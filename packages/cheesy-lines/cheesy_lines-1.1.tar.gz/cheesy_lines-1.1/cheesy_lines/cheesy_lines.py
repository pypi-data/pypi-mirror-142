class cheesy:
    num = int(input("enter num between 0-4"))
    def cheesy_lines(num):
        import random as rand
        cheesy_lines_list = ["Aside from being sexy, what do you do for a living", "Hey, my name’s Microsoft. Can I crash at your place tonight?"
        "Do you like raisins? How do you feel about a date?", "If I could rearrange the alphabet, I’d put ‘U’ and ‘I’ together.", 
        "Are you a parking ticket? Because you’ve got FINE written all over you.", "How about u ram my hard drive eh ;)",]
        cheesy_line = cheesy_lines_list[num]
        print(cheesy_line)
    cheesy_lines(num)