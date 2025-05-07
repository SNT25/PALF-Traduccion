init 1 python:
    class Book:
        # Style can be:
        # novel, newspaper, notebook.
        # String should be exact for best results.
        def __init__(self, style="novel"):
            self.page_list = []
            self.image_dict = {}
            if style in ["novel", "newspaper", "notebook"]:
                self.book_style = style
            else: # In case there's a typo, it will default to a novel.
                self.book_style = "novel"

        # Adds a page to the book.
        # content: The actual string information to add.
        # page_image: The image(s) to add to the page.
        # include_para_tab: If True, makes every line break have a tab on the next paragraph. If False, does not.
        # Note that every one of the above is optional. You can legit have an empty page if you want.
        def Add_Page(self, content=None, page_image=None, include_para_tab=True):
            created_page = self.__Add_Page_Internal(content=content, page_image=page_image, include_para_tab=include_para_tab)
            current_page = len(self.page_list)

            # This code is here in case the user puts in more than 20 lines of content into a single string object.
            # It isn't exactly intended behavior, but I still want to support it for ease of use.
            # In this case, it will automatically make additional pages following the first.
            # A drawback of this method is that you can only put an image on the 1st page of something like this.
            # So if you want images, you need to call an Add_Page for each, and can't make your pages too long.
            # But if some madlad puts an entire novel inside a single string object... this should handle it.
            while len(created_page) > 20:
                self.page_list.append(created_page[:20])
                created_page = created_page[20:]

            # The normal case, once the remaining page lines are 20 or less. (20 is the amount of line supported per page currently.)
            self.page_list.append(created_page)

            # No image, can return early.
            if page_image == None:
                return
            
            # Supporting string for 1 image, list for many.
            if isinstance(page_image, str):
                self.image_dict[current_page] = [page_image]
            else:
                self.image_dict[current_page] = page_image
            

        def Show_Page(self, page_number):
            
            # Trying to view beyond created pages, return nothing. May occur when uneven number of pages.
            if page_number >= len(self.page_list):
                return []

            return self.page_list[page_number]

        def __Add_Page_Internal(self, content=None, page_image=None, include_para_tab=True):

            if content is None and page_image is None: # Blank. What?
                return []
            elif content is None: # Image only.
                return []
            else: # Image and text, or Text only.
                return self.__Book_Mixed_Use(content, page_image, include_para_tab)

                # Must have text, can be used with image on side.
        
        def __Book_Mixed_Use(self, page, page_image=None, include_para_tab=True):
            
            page_list = []
            line_length = 50
            current_line = 0

            # This code is to allow for the user to enter a single string in two formats (string and list), and if string, convert to list on the backend.
            # This is for ease of use.
            all_pages = page
            if isinstance(all_pages, str):
                all_pages = [all_pages]

            for item in all_pages:
                if (item == ""):
                    page_list.append(" ")
                    current_line += 1
                    continue

                page_letters = item
                current_index = 0
                if include_para_tab:
                    page_letters = "       " + page_letters
                total_length = count_non_brace_chars(page_letters)

                while current_index < total_length:
                    if page_image is not None:
                        if current_line >= 6 and current_line <= 14:
                            line_length = 22
                        else:
                            line_length = 50

                    index_end = current_index + line_length - 1
                    if index_end >= total_length or count_non_brace_chars(page_letters) <= index_end + 1: # Just print what is left.
                        page_list.append(page_letters[current_index:])
                        current_index += line_length
                    elif page_letters[index_end].isspace() or page_letters[index_end + 1].isspace(): # Print the next line_length letters, no problems.
                        page_list.append(page_letters[current_index:index_end + 1])
                        current_index += line_length
                    else: # Don't want to cut off a word mid-word, find where it began, put it on the next page.

                        search_attempts = 0
                        while search_attempts < line_length:
                            if page_letters[index_end].isspace(): # We want to end it here.
                                page_list.append(page_letters[current_index:index_end + 1])
                                current_index += line_length - search_attempts
                                break
                            else: # Keep looking.
                                search_attempts += 1
                                index_end -= 1

                        if search_attempts == line_length: # Fine, it's a long word. I'll just print the whole thing.
                            page_list.append(page_letters[current_index:current_index + line_length])
                            current_index += line_length
                    
                    current_line += 1

            return page_list