import glob
import os
import re

import markdown
from requests.auth import HTTPBasicAuth

from .confluence_api import ConfluenceAPI
from .utils.io_helper import file_loader, full_path
from .utils.singleton import Singleton
from .utils.exception import GErrroNotFound


class ConfluenceWrapper(metaclass=Singleton):
    """It would help to update the markdown documents to the conflunce space.
    You could specify a page id to identify a parent page containing all the
    documents.

    """

    def __init__(self):
        pass

    def credential(self, user: str, token: str):
        ConfluenceAPI().auth = HTTPBasicAuth(user, token)

    def update(self, filters=[], force=False):
        """Represent the function to update documents.

        Keyword Arguments:
            filters {list} -- Represent the specific doc names. empty lists
            means updating all documents. (default: {[]})
            force {bool} -- Represent the flag of uploading attachments (Image).
            (default: {False})
        """

        # parse the full path of the doc folder
        doc_path = full_path(path='doc')
        # iterate the doc lists
        for file_name in [item[:-3] for item in glob.glob1(doc_path, '*.md')]:
            if not filters or file_name in filters:
                # load mardown text
                md_full_text = file_loader(os.path.join(doc_path, f'{file_name}.md'))
                symbol_text = list(filter(None, md_full_text.splitlines()))[-1]
                # The last line of each single markdown doc would need to specify
                # the confluence space name and the parent page ID.
                # e.g., @MAR#P854425601
                # @MAR means: "MAR" space
                # #P854425601 means: the parent page id (854425601)
                searched_ctx = re.search(r'^@(\w+)#P(\d+)', symbol_text, re.IGNORECASE)
                if searched_ctx:
                    space_name = searched_ctx[1]
                    parent_page_id = int(searched_ctx[2])
                else:
                    raise GErrroNotFound(message=f'Not found page symbol: {file_name}')
                    continue

                # convert embedded image into attachment marco format
                # if the 'force' parameter was specified, the attached images would be
                # uploaded/updated to the page attachments.
                doc_content, images = self.resolve_ref_image(content=md_full_text)

                print(images)
                # convert markdown text into xhtml format
                doc_content = markdown.markdown(doc_content,
                                                extensions=['extra'],
                                                output_format='xhtml')

                # get confluence page title
                title = file_name.replace('_', ' ')

                page_metadata = ConfluenceAPI().create_or_update_page(title=title,
                                                                      parent_page_id=parent_page_id,
                                                                      space=space_name,
                                                                      xhtml=doc_content)
                if force:
                    # get existing attachment lists
                    attachments = ConfluenceAPI().get_attachments(page_id=page_metadata['id'])
                    # update attachment
                    for image in images:
                        base_name = os.path.basename(image)
                        image_path = full_path(os.path.join('doc', image))
                        media_id = attachments.get(base_name, None)
                        if media_id:
                            # remove the old version attachment
                            # this is a known issue that the media could not display correctly
                            # when updating a new revision to override. We would need to delete
                            # the attachment before uploading a new version.
                            ConfluenceAPI().remove_attachment(media_id=media_id)

                        # upload the new version of the attached media
                        ConfluenceAPI().update_attachment(page_id=page_metadata['id'],
                                                          file_name=base_name,
                                                          file_path=image_path,
                                                          attachment_id=attachments.get(base_name, None))

    def resolve_ref_image(self, content):
        """Go through all doc content, resolve the image elements with
        confluence attachment.

        Arguments:
            content {str} -- xhtml doc full text.

        Returns:
            {str} -- Represent the resolved xhtml doc full text.
            {str} -- Represent the image lists. It would be used to perform
            the uploading attachment through confluence api.
        """
        text_lines = [x.strip() for x in content.splitlines()]
        image_lists = []
        results = []
        for row in text_lines:
            pattern = re.compile(r'(\!\[[\w\s\,0-9]{1,}\]\(images\/[\w_\.\/]{1,}\))')
            matched_groups = pattern.findall(row)
            if matched_groups:
                for item in matched_groups:
                    image_matched = re.search(r'\!\[([\w\s\,0-9]{1,})\]\((images\/[\w_\.\/]{1,})\)', item)
                    image_lists.append(image_matched[2])
                    attachment = f'<ri:attachment ri:filename="{os.path.basename(image_matched[2])}" />'
                    image_props = image_matched[1].split(',')
                    if len(image_props) != 3:
                        image_props = (image_matched[1], 'center', '680')

                    image_item = f'<ac:image ac:align="{image_props[1]}" ac:layout="{image_props[1]}" ac:width="{image_props[2]}">{attachment}</ac:image>'
                    row = row.replace(item, image_item)
            results.append(row)

        return '\n'.join(results), image_lists
