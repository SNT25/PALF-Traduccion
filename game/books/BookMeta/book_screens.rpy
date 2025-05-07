screen book_mixed_text(book):
    modal True
    zorder 11

    add "BG/Blank2.webp" alpha 0.3
    add "BG/flashback.webp" alpha 0.5 matrixcolor InvertMatrix()

    on "show" action SetVariable('book_page_at', 0)
    on "show" action SetVariable('open_book_total_pages', len(book.page_list))

    if book.book_style == "notebook":
        add "images/GUI/book/notebook.webp"
    elif book.book_style == "newspaper":
        add "images/GUI/book/newspaper.webp"
    elif book.book_style == "novel":
        add "images/GUI/book/novel.webp"
    
    use show_two_pages(book_page_at, book)

    # Add transparent imagebuttons on sides of book to move left and right at x.
    imagebutton idle Solid('#00000000') pos (940, 115) xysize (775, 925) anchor (1.0,0) action If(book_page_at != 0, SetVariable("book_page_at", book_page_at - 2))
    imagebutton idle Solid('#00000000') pos (980, 115) xysize (775, 925) anchor (0,0) action If(book_page_at + 2 < len(book.page_list), SetVariable("book_page_at", book_page_at + 2))

    # The tabs.
    imagebutton idle Solid('#00000000') hover "images/GUI/book/TabExit.webp" pos (249, 2) xysize (87,99) action [Hide("show_two_pages"), Hide("book_mixed_text"), Hide("search_page")]
    imagebutton idle Solid('#00000000') hover "images/GUI/book/TabLeftFar.webp" pos (423, 2) xysize (87,99) action SetVariable("book_page_at", max(0, book_page_at - 40))
    imagebutton idle Solid('#00000000') hover "images/GUI/book/TabLeftMed.webp" pos (597, 2) xysize (87,99) action SetVariable("book_page_at", max(0, book_page_at - 10))
    imagebutton idle Solid('#00000000') hover "images/GUI/book/TabLeft.webp" pos (771, 2) xysize (87,99) action SetVariable("book_page_at", max(0, book_page_at - 2))
    imagebutton idle Solid('#00000000') hover "images/GUI/book/TabRight.webp" pos (1062, 2) xysize (87,99) action If(open_book_total_pages % 2 == 0, SetVariable("book_page_at", min(open_book_total_pages - 2, book_page_at + 2))), If(len(book.page_list) % 2 == 1, SetVariable("book_page_at", min(open_book_total_pages - 1, book_page_at + 2)))
    imagebutton idle Solid('#00000000') hover "images/GUI/book/TabRightMed.webp" pos (1236, 2) xysize (87,99) action If(open_book_total_pages % 2 == 0, SetVariable("book_page_at", min(open_book_total_pages - 2, book_page_at + 10))), If(len(book.page_list) % 2 == 1, SetVariable("book_page_at", min(open_book_total_pages - 1, book_page_at + 10)))
    imagebutton idle Solid('#00000000') hover "images/GUI/book/TabRightFar.webp" pos (1410, 2) xysize (87,99) action If(open_book_total_pages % 2 == 0, SetVariable("book_page_at", min(open_book_total_pages - 2, book_page_at + 40))), If(len(book.page_list) % 2 == 1, SetVariable("book_page_at", min(open_book_total_pages - 1, book_page_at + 40)))
    imagebutton idle Solid('#00000000') hover "images/GUI/book/TabSearch.webp" pos (1584, 2) xysize (87,99) action ToggleScreen("search_page")

    
screen show_two_pages(index, book):
    viewport id "page":
        area(940,115,755,910)
        xanchor 1.0

        vbox:
            spacing 10

            for line in book.Show_Page(index):
                $ line = line.replace("first_name", first_name)
                text line
                

    viewport id "page2":
        area(1000,115,755,910)
        
        vbox:
            spacing 10

            for line in book.Show_Page(index + 1):
                $ print(line)
                $ line = line.replace("first_name", first_name)
                $ print(line)
                $ print("\n\n\n")
                text line
    
    if index in book.image_dict:
        # Display an image.
        if len(book.image_dict[index]) == 1 and len(book.page_list[index]) != 0: # There's actually text here.
            add book.image_dict[index][0] pos (735, 590) anchor (0.5,0.5) xysize (380,380) fit "contain"
        else:
            # X area begins at 185, ends at 940.
            if len(book.image_dict[index]) == 1:
                add book.image_dict[index][0] pos (563, 570) anchor (0.5,0.5) xysize (750,750) fit "contain"
            elif len(book.image_dict[index]) == 2:
                add book.image_dict[index][0] pos (563, 340) anchor (0.5,0.5) xysize (450,450) fit "contain"
                add book.image_dict[index][1] pos (563, 795) anchor (0.5,0.5) xysize (450,450) fit "contain"
            elif len(book.image_dict[index]) == 3:
                add book.image_dict[index][0] pos (185, 340) anchor (0,0.5) xysize (450,450) fit "contain"
                add book.image_dict[index][1] pos (935, 567) anchor (1.0,0.5) xysize (450,450) fit "contain"
                add book.image_dict[index][2] pos (185, 795) anchor (0,0.5) xysize (450,450) fit "contain"
            elif len(book.image_dict[index]) == 4:
                add book.image_dict[index][0] pos (373, 340) anchor (0.5,0.5) xysize (376,376) fit "contain"
                add book.image_dict[index][1] pos (752, 340) anchor (0.5,0.5) xysize (376,376) fit "contain"
                add book.image_dict[index][2] pos (373, 795) anchor (0.5,0.5) xysize (376,376) fit "contain"
                add book.image_dict[index][3] pos (752, 795) anchor (0.5,0.5) xysize (376,376) fit "contain"

    if index + 1 in book.image_dict:
        # Display an image.
        if len(book.image_dict[index + 1]) == 1 and len(book.page_list[index + 1]) != 0: # There's actually text here.
            add book.image_dict[index + 1][0] pos (1550, 590) anchor (0.5,0.5) xysize (380,380) fit "contain"
        else:
            # X area begins at 1000, ends at 1755.
            if len(book.image_dict[index + 1]) == 1:
                add book.image_dict[index + 1][0] pos (1377, 570) anchor (0.5,0.5) xysize (750,750) fit "contain"
            elif len(book.image_dict[index + 1]) == 2:
                add book.image_dict[index + 1][0] pos (1377, 340) anchor (0.5,0.5) xysize (450,450) fit "contain"
                add book.image_dict[index + 1][1] pos (1377, 795) anchor (0.5,0.5) xysize (450,450) fit "contain"
            elif len(book.image_dict[index + 1]) == 3:
                add book.image_dict[index + 1][0] pos (1750, 340) anchor (1.0,0.5) xysize (450,450) fit "contain"
                add book.image_dict[index + 1][1] pos (1005, 567) anchor (0.0,0.5) xysize (450,450) fit "contain"
                add book.image_dict[index + 1][2] pos (1750, 795) anchor (1.0,0.5) xysize (450,450) fit "contain"
            elif len(book.image_dict[index + 1]) == 4:
                add book.image_dict[index + 1][0] pos (1188, 340) anchor (0.5,0.5) xysize (376,376) fit "contain"
                add book.image_dict[index + 1][1] pos (1567, 340) anchor (0.5,0.5) xysize (376,376) fit "contain"
                add book.image_dict[index + 1][2] pos (1188, 795) anchor (0.5,0.5) xysize (376,376) fit "contain"
                add book.image_dict[index + 1][3] pos (1567, 795) anchor (0.5,0.5) xysize (376,376) fit "contain"

    text str(index + 1) size 26 pos (167, 1022)
    text str(index + 2) size 26 pos (1752, 1022) xanchor 1.0

# This screen is the page which displays the search bar inside of a book.    
screen search_page():
    zorder 12

    frame:
        xysize (160,85) 
        style "menu_choice_button"
        xpos 1584
        ypos 101
        xanchor 0
        imagebutton idle Solid('#00000000') action NullAction()

        vbox:
            hbox:
                text " {size=+2}Page:"
                add Input(hover_color="#f0f0f0",size=40, color="#000", default=int(book_page_at) + 1, changed=book_page_func, length=3, button=renpy.get_widget("search_page","input_1")) yalign 0 

            hbox:
                textbutton " {b}Enter{/b}" style "buttonhover" action Hide("search_page")


init python:
    # This function provides the ability to change pages inside of the Book currently open.
    def book_page_func(newstring):
        global book_page_at
        global open_book_total_pages

        if newstring.isdigit() and int(newstring) > 0 and newstring != "":

            newstring = str(int(newstring) - 1)
            
            if int(newstring) >= open_book_total_pages:
                newstring = open_book_total_pages - 1

            if int(newstring) % 2 == 1:
                book_page_at = int(newstring) - 1
            else:    
                book_page_at = int(newstring)
        elif newstring == "":
            book_page_at = 0


init 2 python:

    # The below two variables are REQUIRED, and MUST NOT be removed. Seriously, it'd break everything.
    book_page_at = 0
    open_book_total_pages = 0


init 2 python:
    # The following will show an example book, giving an overview of the many features that this tool provides.

    # Strings for some basic pages.
    example_page = "What is the meaning of this? What is the meaning of this? What is the meaning of this? What is the meaning of this? What is the meaning of this? What is the meaning of this? What is the meaning of this? What is the meaning of this? What is the meaning of this? What is the meaning of this? What is the meaning of this? What is the meaning of this? What is the meaning of this? What is the meaning of this? What is the meaning of this? What is the meaning of this? What is the meaning of this? What is the meaning of this? What is the meaning of this? What is the meaning of this? What is the meaning of this? What is the meaning of this? What is the meaning of this? What is the meaning of this? What is the meaning of this? What is the meaning of this? What is the meaning of this? What is the meaning of this? What is the meaning of this? What is the meaning of this? What is the meaning of this? What is the meaning of this? What is the meaning of this? What is the meaning of this? What is the meaning of this? What is the meaning of this? hi hi hi hi hi hi hi hi hi hi hi hi hi hi hi hi hi hi hi hi hi hi hi hi hi hi hi hi hi hi hi hi hi hi hi hi hi hi hi hi hi hi hi hi hi hi hi hi hi MERRY CHRISTMAS HO HO HO HO HO HO HO HO HO HO HO HO HO HO HO HO HO HO HO HO HO HO HO HO HO HO HO HO HO HO HO HO HO HO HO HO HO HO HO HO WOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO"
    flareon_page = "Hey guys, did you know that in terms of human companionship, Flareon is objectively the most huggable Pokemon? While their maximum temperature is likely too much for most, they are capable of controlling it, so they can set themselves to the perfect temperature for you. Along with that, they have a lot of fluff, making them undeniably incredibly soft to touch. But that's not all, they have a very respectable special defense stat of 110, which means that they are likely very calm and resistant to emotional damage. Because of this, if you have a bad day, you can vent to it while hugging it, and it won't mind. It can make itself even more endearing with moves like Charm and Baby Doll Eyes, ensuring that you never have a prolonged bout of depression ever again. Hey guys, did you know that in terms of human companionship, Flareon is objectively the most huggable Pokemon? While their maximum temperature is likely too much for most, they are capable of controlling it, so they can set themselves to the perfect temperature for you. Along with that, they have a lot of fluff, making them undeniably incredibly soft to touch. But that's not all, they have a very respectable special defense stat of 110, which means that they are likely very calm and resistant to emotional damage. Because of this, if you have a bad day, you can vent to it while hugging it, and it won't mind. It can make itself even more endearing with moves like Charm and Baby Doll Eyes, ensuring that you never have a prolonged bout of depression ever again. Hey guys, did you know that in terms of human companionship, Flareon is objectively the most huggable Pokemon? While their maximum temperature is likely too much for most, they are capable of controlling it, so they can set themselves to the perfect temperature for you. Along with that, they have a lot of fluff, making them undeniably incredibly soft to touch. But that's not all, they have a very respectable special defense stat of 110, which means that they are likely very calm and resistant to emotional damage. Because of this, if you have a bad day, you can vent to it while hugging it, and it won't mind. It can make itself even more endearing with moves like Charm and Baby Doll Eyes, ensuring that you never have a prolonged bout of depression ever again."
    
    # Creating a string with a linebreak, and other effects such as bold, italize.
    example_page_larvesta = ["{glitch=10.0}{b}{i}Larvesta stolen!", "Breaking news! A Larvesta egg was taken by the villainous Red!", "{b}The victim of this heinous crime is reported to be May Birch, a Hoenn native.",
    "Her boyfriend, Brendan, attempted to stop this by using his Pokémon, but he was summarily defeated.", 
    "When interviewing the suspect, our reporters commented about how May was crying.", "His response? ''This ain't about her, I just wanted the egg.''", "Kobukan weekly will continue to have updates of this ongoing story, as well as the election results next week!"]
    
    # Iusti's favorite.
    latias_copypasta = "{b}Hey guys, did you know that in terms of human and Pokémon travel partners, a Latias' forehead is proportionally sized and perfectly shaped to fit the average human hand? This means that when you give them a headpat, you are able to provide stimulation to the 5 sensitive nerve spots around its head & ears all at the same time with minimal movement and effort causing a healthy release of dopamine which thus relaxes its muscles that they constantly put a strain on in order to fly at incredibly high speeds for long distances. This makes them the perfect travel partner because the constantly desire your affection through headpats."

    example_book = Book("novel") # You can pass in the styles: notebook, novel, newspaper. Try them all out!
    example_book.Add_Page(example_page_larvesta, "Pokemon/636.webp")
    example_book.Add_Page(latias_copypasta, "Pokemon/380.webp")
    example_book.Add_Page(flareon_page, "Pokemon/136.webp")

    # Examples of how images can be displayed on their own page.
    # Images can be of any shape (and their dimensions will be preserved), but square will usually show up best.
    # Up to 4 images per page are supported.
    example_book.Add_Page(None, "Pokemon/380.webp")
    example_book.Add_Page(None, ["Pokemon/380.webp", "Pokemon/380.webp"])
    example_book.Add_Page(None, ["Pokemon/380.webp", "Pokemon/380.webp", "Pokemon/380.webp"])
    example_book.Add_Page(None, ["Pokemon/380.webp", "Pokemon/380.webp", "Pokemon/380.webp", "Pokemon/380.webp"])
    
    # This is the example of behavior when the page has too many words for a single page: it creates a new page on its own. 
    # It will do this for as long as needed to display the entire string.
    bee_movie = " According to all known laws of aviation, there is no way a bee should be able to fly. Its wings are too small to get its fat little body off the ground. The bee, of course, flies anyway because bees don't care what humans think is impossible. Yellow, black. Yellow, black. Yellow, black. Yellow, black. Ooh, black and yellow! Let's shake it up a little. Barry! Breakfast is ready! Ooming! Hang on a second. Hello? - Barry? - Adam? - Oan you believe this is happening? - I can't. I'll pick you up. Looking sharp. Use the stairs. Your father paid good money for those. Sorry. I'm excited. Here's the graduate. We're very proud of you, son. A perfect report card, all B's. Very proud. Ma! I got a thing going here. - You got lint on your fuzz. - Ow! That's me! - Wave to us! We'll be in row 118,000. - Bye! Barry, I told you, stop flying in the house! - Hey, Adam. - Hey, Barry. - Is that fuzz gel? - A little. Special day, graduation. Never thought I'd make it. Three days grade school, three days high school. Those were awkward. Three days college. I'm glad I took a day and hitchhiked around the hive. You did come back different. - Hi, Barry. - Artie, growing a mustache? Looks good. - Hear about Frankie? - Yeah. - You going to the funeral? - No, I'm not going. Everybody knows, sting someone, you die. Don't waste it on a squirrel. Such a hothead. I guess he could have just gotten out of the way. I love this incorporating an amusement park into our day. That's why we don't need vacations. Boy, quite a bit of pomp... under the circumstances. - Well, Adam, today we are men. - We are! - Bee-men. - Amen! Hallelujah! Students, faculty, distinguished bees, please welcome Dean Buzzwell. Welcome, New Hive Oity graduating class of... ...9:15. That concludes our ceremonies. And begins your career at Honex Industries! Will we pick ourjob today? I heard it's just orientation. Heads up! Here we go. Keep your hands and antennas inside the tram at all times. - Wonder what it'll be like? - A little scary. Welcome to Honex, a division of Honesco and a part of the Hexagon Group. This is it! Wow. Wow. We know that you, as a bee, have worked your whole life to get to the point where you can work for your whole life. Honey begins when our valiant Pollen Jocks bring the nectar to the hive. Our top-secret formula is automatically color-corrected, scent-adjusted and bubble-contoured into this soothing sweet syrup with its distinctive golden glow you know as... Honey! - That girl was hot. - She's my cousin! - She is? - Yes, we're all cousins. - Right. You're right. - At Honex, we constantly strive to improve every aspect of bee existence. These bees are stress-testing a new helmet technology. - What do you think he makes? - Not enough. Here we have our latest advancement, the Krelman. - What does that do? - Oatches that little strand of honey that hangs after you pour it. Saves us millions. Oan anyone work on the Krelman? Of course. Most bee jobs are small ones. But bees know that every small job, if it's done well, means a lot. But choose carefully because you'll stay in the job you pick for the rest of your life. The same job the rest of your life? I didn't know that. What's the difference? You'll be happy to know that bees, as a species, haven't had one day off in 27 million years. So you'll just work us to death? We'll sure try. Wow! That blew my mind! ''What's the difference?'' How can you say that? One job forever?"

    example_book.Add_Page(bee_movie)
    example_book.Add_Page(example_page)    

    # If you want, you can add a page to a book and have it be completely empty.
    example_book.Add_Page()

    # How to send a LayeredImage into the book.
    # This can be done for any character.
    example_book.Add_Page(None, "red uniform angrymouth angryeyes")

    # Examples of how to Crop a character image into the book.
    # Note that for the dimensions, you must account for the zoom in the portraits.
    # As most character zooms are .5, you will actually need to divide the dimensions of the real image by 2.
    example_book.Add_Page(None, [Crop( (325, 300, 350, 450), "erika happymouth closedeyes" )])
    example_book.Add_Page(None, [Crop( (290, 260, 385, 465), "bianca neutral shadow furiouseyes angryeyebrows carethappy lightblush " )])
    example_book.Add_Page(None, [Crop( (325, 300, 350, 450), "erika happymouth closedeyes" ), Crop( (290, 260, 385, 465), "bianca neutral shadow furiouseyes angryeyebrows carethappy lightblush " )])
    example_book.Add_Page(None, [Crop( (290, 260, 385, 465), "bianca neutral heart angryeyebrows happymouth mediumblush" ), Crop( (290, 260, 385, 465), "bianca neutral shadow furiouseyes angryeyebrows carethappy lightblush " ), Crop( (290, 260, 385, 465), "bianca uniform tired blankeyes angryeyebrows furious2mouth mediumblush cry" ), Crop( (290, 260, 385, 465), "bianca neutral dots shockedeyebrows o fullblush " )])
    example_book.Add_Page(None, [Crop( (290, 260, 385, 465), "bianca neutral heart angryeyebrows happymouth mediumblush" ), Crop( (290, 260, 385, 465), "bianca neutral shadow furiouseyes angryeyebrows carethappy lightblush " ), Crop( (290, 260, 385, 465), "bianca uniform tired blankeyes angryeyebrows furious2mouth mediumblush cry" ), Crop( (290, 260, 385, 465), "bianca neutral dots shockedeyebrows o fullblush " )])

    # It is likely possible to do much more with these images as well before passing them into the page, should be very flexible.
