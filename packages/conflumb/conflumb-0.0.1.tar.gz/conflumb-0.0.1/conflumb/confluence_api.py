import json
import mimetypes

import requests
import wrapt

from .utils.singleton import Singleton
from .utils.exception import GErrorConfluenceAPIOffline

CONFLUENCE_API_URL = 'https://voteb.atlassian.net/wiki/rest/api'

MAX_RETRY_TIMES = 3

ARG_ARGUMENT = 'argument'
ARG_CQL = 'cql'
ARG_FILES = 'files'
ARG_HEADERS = 'headers'
ARG_MODE = 'mode'
ARG_PAYLOAD = 'payload'
ARG_VERSION = 'version'


@wrapt.decorator
def call_confluence_api(wrapped, instance, args, kwargs):
    result = {'text': None}
    if wrapped.__name__ == 'search':
        url = f'{CONFLUENCE_API_URL}/content/search?cql=({kwargs[ARG_CQL]})'
    else:
        url = f'{CONFLUENCE_API_URL}/{wrapped.__name__}'
        if args:
            url = f'{url}/{"/".join(args)}'

    # append custom headers for requrests
    header = {}  # ConfluenceHelper().header
    if ARG_HEADERS in kwargs:
        header.update(kwargs[ARG_HEADERS])

    result = None
    retry = 1
    while(True):
        try:
            result = requests.request(
                kwargs.get(ARG_MODE, 'GET'),
                url,
                data=json.dumps(kwargs.get(ARG_PAYLOAD)) if ARG_PAYLOAD in kwargs else None,
                params=kwargs.get(ARG_ARGUMENT, None),
                files=kwargs.get(ARG_FILES, None),
                headers=header,
                auth=instance.auth)
            result.raise_for_status()
            break
        except Exception as e:
            if retry >= MAX_RETRY_TIMES:
                raise GErrorConfluenceAPIOffline(
                    "Confluence API is not able to be used or obtained!", result.text)
            else:
                retry += 1
    # if result.status_code == 200 else result.text)
    return wrapped(None, response=result.json() if result.status_code == 200 else result.text)


class ConfluenceAPI(metaclass=Singleton):
    def __init__(self):
        self.auth = None

    @call_confluence_api
    def content(self, *args, **kwargs):
        return kwargs['response']

    @call_confluence_api
    def search(self, *args, **kwargs):
        return kwargs['response']

    def get_page_content(self, page_id):
        # data = json.loads(json.dumps(content('{}?expand=body.storage'.format(page_id))))
        data_html = self.content(f'{page_id}?expand=body.storage')['body']['storage']['value']
        return data_html

    # def get_page_ancestors(page_id=None):
    #     """
    #     TODO: the 'ancestors' property could not be parsed properly when the page was just created.
    #     if you met the error message of missing ancestors from the function, just run the 'edoc'
    #     command again. I would suggest to split the process from creating new pages and update the
    #     contents for the pages.

    #     Keyword Arguments:
    #         page_id {[type]} -- [description] (default: {None})
    #     """
    #     return content('{}?expand=ancestors'.format(page_id)).get('ancestors', None)

    def get_page_info(self, page_id=None):
        return self.content(page_id)

    def update_confluence_page(self, page_id=None, title=None, xhtml=None):
        extra_headers = {
            'content-type': 'application/json',
        }
        info = self.get_page_info(page_id=page_id)

        ver = int(info['version']['number']) + 1 if ARG_VERSION in info else 1

        payload = {
            'id': page_id,
            "type": "page",
            "title": title,
            "status": "current",
            "version": {
                "number": ver
            },
            "body": {
                'storage':
                {
                    'representation': 'storage',
                    'value': str(xhtml),
                }
            }
        }

        # # hook up ['ancestors'] for updating existing page
        # # skip appending ancestors when creating new page
        # ancestors = get_page_ancestors(page_id=page_id)
        # if ancestors:
        #     anc = ancestors[-1]
        #     del anc['_links']
        #     del anc['_expandable']
        #     del anc['extensions']

        #     payload.update({
        #         'ancestors': [anc]
        #     })

        result = self.content(page_id, payload=payload, mode='PUT', headers=extra_headers)
        return result

    def create_or_update_page(self, title=None, parent_page_id=None, space='Savoia', xhtml=None):
        # perform a search first with the title before creating a new page
        page = next(iter(self.adv_search(cql=f"title='{title}'")), None)

        if not page:
            extra_headers = {
                'content-type': 'application/json',
            }
            payload = {
                "type": "page",
                "title": title,
                "space": {
                    "key": space.upper()
                },
                "ancestors": [
                    {
                        "id": parent_page_id
                    }
                ],
                "body": {
                    "storage": {
                        "value": 'PLACEHOLDER',
                        "representation": "storage"
                    }
                }
            }
            page = self.content(payload=payload, mode='POST', headers=extra_headers)

        if 'id' in page and xhtml:
            self.update_confluence_page(page['id'], title=title, xhtml=xhtml)

        return page

    def remove_attachment(self, media_id=None):
        self.content(f'{media_id}?status=current', mode='DELETE')
        return True

    def get_attachments(self, page_id=None):
        results = self.content(f'{page_id}/child/attachment?limit=2000')
        return {item['title']: item['id'] for item in results['results']} if results else {}

    def update_attachment(self, page_id=None, file_name=None, file_path=None, attachment_id=None):
        """Create or update attachment to the specific confluence page

        Keyword Arguments:
            page_id {str} -- Represent the confluence page id (default: {None})
            data {blob} -- Represent the attachment file data (binary) (default: {None})
        """

        extra_headers = {
            "X-Atlassian-Token": "nocheck"
        }
        url = f'{page_id}/child/attachment'
        if attachment_id:
            url = f'{url}/{attachment_id}/data'

        # determine content-type
        content_type, _ = mimetypes.guess_type(file_path)
        if content_type is None:
            content_type = 'multipart/form-data'

        # provide content-type explicitly
        files = {'file': (file_name, open(file_path, 'rb'), content_type)}

        return self.content(url,
                            mode='POST',
                            headers=extra_headers,
                            files=files)

    def adv_search(self, key=None, cql=None):
        result = {'results': []} if not cql else self.search(cql=cql)
        if 'results' in result:
            return [item[key] if key and key in item else item for item in result['results']]
        else:
            return []
