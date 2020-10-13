define h = Character(_("HARU"), color="BE90F4", who_outlines=[ (8, "#FFFFFF") ])
define e = Character(_("ERIKA"), color="953C60", who_outlines=[ (8, "#FFFFFF") ])
define m = Character(_("MANAMI"), color="BDD8F8", who_outlines=[ (8, "#FFFFFF") ])
define q = Character(_("???"), who_outlines=[ (8, "#FFFFFF") ])
define f = Character(_("FRONT DESK"), who_outlines=[ (8, "#FFFFFF") ])
define s = Character(_("STAFF"), who_outlines=[ (8, "#FFFFFF") ])
define he = Character(_("{color=#BE90F4}HARU{/color} & {color=#953C60}ERIKA{/color}"), who_outlines=[ (8, "#FFFFFF") ])
define hme = Character(_("{color=#BE90F4}HARU{/color} & {color=#953C60}ERIKA{/color} & {color=#BDD8F8}MANAMI{/color}"), who_outlines=[ (8, "#FFFFFF") ])

define n = Character("")

define ending = Character("", kind=nvl)

define fade = Fade(0.5, 3.0, 0.5)

label splashscreen:
    scene black










label languagechoose:
    if not persistent.languagepick:
        $ renpy.change_language(None)
        call screen language with dissolve

        $ persistent.languagepick = True

        menu:
            "Would you like to use hints?"
            "Yes":
                $ persistent.hintheart = True
            "No":
                $ persistent.hintheart = False

    pause(0.5)
    scene splashscreen with dissolve
    pause(1.5)

    return

label start:

    $ rotenburo = 0
    $ shower = 0
    $ lie = 0
    $ reply = 0
    $ talk = 0
    $ womensbath = 0
    $ yes = 0
    $ hiroen = 0
    $ present = 0

    $ spoons = 3








    stop music fadeout 1.0
    scene cg harubed 4
    with fade
    play music "music/ringtone.ogg" fadein 2.0
    pause(3.0)
    scene cg harubed 0 with dissolve
    h "Who on earth could be calling me...?"
    scene cg harubed 1 with dissolve
    stop music
    play sound "music/beepbeep.ogg"
    "...*beep*..."
    play music "music/bedroom.ogg" fadeout 2.0
    scene cg harubed 2 with dissolve
    m "Haru! It's been so long since I've talked to you!"
    m "Sorry for calling so suddenly! You're not busy, are you?"
    h "Not busy at all. How've you been, Manami?"
    m "I've been wonderful, thanks! And that's why I wanted to call you."
    m "My birthday is coming up, and since it's my 20th, my parents said they would let me go on a trip with my friends!"
    m "So, my plan is to go on a trip to the hot springs with my two best friends..."
    m "And of course that includes you."
    m "My parents will pay for everything, so don't worry about the cost!"
    h "Hot springs? But you know that I'm..."
    m "I know, I know. Which is why I'm calling to talk to you first before deciding anything."
    m "Haru, you're my oldest and closest friend."
    m "It would mean so much to me if you were with me to celebrate my 20th birthday."
    m "But I also want you to enjoy yourself to the fullest."
    m "So let me know what I can do to make you as comfortable as possible."
    h "But it's been years since I've been to a public bath, let alone a hot spring..."
    m "I know! Which is why it's a good chance. You'll be with me! So if anything or anyone bothers you, you can tell me."
    h "I'm not really worried about me being uncomfortable - it's more everyone else..."
    m "It'll be fine! Nobody will pay any attention."
    h "They will."
    m "Haru, nobody cares as much as you think they do. I promise."
    m "Please come. For me...?"
    menu:
        h "(What should I say?)"
        "...If they have reserved baths.":
            h "Fine... If they have reserved baths, I'll go."
            m "Yes! It's going to be the best birthday ever!"
            m "I'll call you again when everything's been sorted out!"
            play sound "music/beep.ogg"
            "...*beep*..."
            scene cg harubed 3 with dissolve
            h "...She always hangs up so fast."
            h "I can't believe I agreed to go to the hot springs..."
            h "What should I do?"
            h "How do women behave when they go to hot springs together?"
            scene cg harubed 1 with dissolve
            h "Let's see what the search terms \"hot springs with female friends\" get me..."
            h "Oh, an article titled \"When Going to the Hot Springs with Your Girlfriends\"."
            h "\"You don't have to care that much about makeup\"? So I should worry about it a little...?"
            h "\"Don't worry about bust size!\" Well, I guess I don't really have a bust to worry about..."
            h "\"But don't forget to shave!\" Wait, shave? Which parts? How much?"
            h "Agh, I just don't know! I'll just have to figure it out as I go!"
            h "I'll just wait until Manami calls with more details..."
            h "This is enough internet for me today."
            scene cg harubed 3 with dissolve
            h "Guess I'll turn in for today..."

            stop music fadeout 2.0
            jump checkin
        "Sorry... I just...":

            $ spoons = 0
            h "Sorry... I just can't..."
            m "Haru..."
            h "Sorry."
            m "...It's OK. I understand."
            m "I'll think of a different plan for my birthday!"
            h "No, don't - you don't have to -"
            m "I'll call you again once I've decided!"
            play sound "music/beep.ogg"
            "...*beep*..."
            scene cg harubed 3 with dissolve
            h "...She hung up."
            h "Manami's the same as usual. I'm glad she's doing well..."
            h "But she's wrong. She says that nobody cares as much as I think they do, but..."
            h "That's because she thinks everybody is as good a person as her. And why wouldn't she?"
            h "She's never had anything happen to prove her otherwise."
            h "Her parents are the best. Always understanding, even about me..."
            h "Her mum even took me shopping for new clothes, after I came out to her."
            h "...They've always been so kind to me. With Manami's birthday trip too."
            h "I bet Manami really wanted to go to the hot springs for her birthday..."
            h "Maybe I shouldn't have said no... I could have just stayed out of the baths."
            h "I guess it's too late now..."
            h "I'll just wait for Manami to contact me again..."
            stop music fadeout 3.0

label bad2:
    $ quick_menu = False
    $ _skipping = False
    scene cg badend2
    with fade
    show text "{font=tl/None/npckc.ttf}NORMAL END)\nLET'S TRY SOMETHING ELSE" at credits with Dissolve(1.5)
    pause
    hide text with dissolve
    show text "{font=tl/None/npckc.ttf}CREDITS\nStory/Code/Art: npckc\nMusic: maxdotine & npckc\nSE: Pocket Sound\n\nThank you for playing!{/font}" at credits with Dissolve(1.5)
    pause
    stop music fadeout 3.0
    scene black with Dissolve(3.0)
    $ persistent.bad2 = True
    $ achievement.grant("bad2")
    $ _skipping = True
    return

label checkin:

    scene bg reception
    show haru hmm at left
    with fade
    play music "music/hotel.ogg" fadeout 2.0
    h "I'm really here..."
    h "What on earth am I doing?"
    h "I'm not really prepared for this..."
    h "But I'm here now. I just have to power through this."
    show haru ganba
    h "You can do it, Haru...!"
    q "Haru! Over here!"
    h "Where?"
    show haru
    show manami at right with easeinright
    h "Hi, Manami."
    m "Oh, WOW, Haru! I love your hair!"
    show haru blush
    h "Thanks... I decided to grow it out."
    m "It looks amazing!"
    h "Thanks, Manami."
    show manami at midright with ease
    show erika at right with easeinright
    show haru
    e "Hey, Manami, don't forget about me!"
    m "Oh, sorry, Erika!"
    m "This is Haru, my childhood friend."
    m "And Haru, this is Erika, my friend from high school."
    e "The last name's Nagata, in case you were wondering."
    h "I'm Haru Suzuki. It's nice to meet you."
    show erika grin
    e "You can speak more casually, y'know. We're the same age."
    h "We're the same age?"
    m "Yup! Or close enough. Erika's 20."
    e "Yeah, I heard from Manami that you two went to the same preschool."
    h "Yes. Er, I mean... Yeah."
    e "Wow, you really need to loosen up. A dip in the hot spring will probably do you some good."
    show erika
    e "Manami, you gonna check us in or what?"
    m "Right! Let's go then."
    show bg reception lady
    f "Welcome."
    m "Hello, I have a reservation under Tachibana."
    f "Yes, we have your reservation! Would you please fill out this registration card?"
    m "Haru, Erika, could you fill out your information?"
    e "Yeah, sure."
    h "OK."
    scene cg form 0
    with dissolve
    h "Time to fill out this form."
    play sound "music/write.ogg"
    h "First, my name..."
    scene cg form 1 with dissolve
    h "...I probably need to write my legal name."
    scene cg form 2 with dissolve
    h "...And my legal gender too."
    scene cg form 3 with dissolve
    h "..."
    h "I should fill out the rest of the form."
    scene cg form 4 with dissolve
    play sound "music/write.ogg"
    h "Age 19..."
    scene cg form 5 with dissolve
    h "Address and occupation..."
    scene cg form 6 with dissolve
    h "And everything else."
    scene bg reception lady
    show haru at left
    show manami at midright
    show erika at right
    with dissolve
    h "I'm finished."
    e "Me too."
    m "Thanks!"
    m "Here is the registration card."
    f "Thank you. Just let me..."
    f "Hm?"
    f "Mr... Haruto Suzuki?"
    menu:
        h "(...I probably need to answer.)"
        "That would be me...":

            $ spoons -= 1
            h "That would be me..."
        "Is there a problem?":
            h "That's me, but is there a problem?"
    f "..."
    f "I see. Your room is the Gingko Room on the second floor."
    f "Please enjoy your stay."
    show haru down
    h "..."
    m "Let's go to our room then!"
    e "I'm gonna buy a drink first. My throat is like a desert."
    e "See you back at the room."
    hide erika with moveoutright
    show manami worried at right with ease
    m "Haru, you OK?"
    show haru tsuyoki
    h "Yup! You don't have to worry about me."
    h "Let's go to the room."
    hide haru with moveoutleft
    m "Haru..."

    jump room

label room:
    scene bg room
    show haru at left
    show manami hehe at midright
    show erika at right
    with fade
    e "Nice! It's a proper tatami room."
    e "Tatami is so much trouble to clean, but I love how it looks..."
    m "I love tatami too... It has such a nice smell."
    m "I just want to lie down and sleep on it..."
    show erika grin
    e "Go ahead. Me and Suzuki here will just head to the hot springs while you're snoozing away."
    show manami surprised
    m "No, don't go without me! I want to go to the hot springs too!"
    e "I'm just kidding."
    show erika
    e "Though I do plan on heading to the hot springs ASAP."
    e "Too much studying hunched over at my desk lately - I need to give my stiff shoulders a break."
    show haru down
    h "Hot springs..."
    e "We should get changed first, I guess?"
    e "The yukata should be around here somewhere..."
    show erika at center with ease
    e "Not here..."
    show erika at midleft with ease
    e "Or here..."
    show manami at right
    show erika at midright
    with ease
    e "Or - "
    show erika grin
    e "Found them! One for each of us."
    m "Ooh, they're cute! I wonder if they're for sale."
    m "Let's get changed, then - "
    show haru panicked
    h "I'll change in the bathroom!"
    hide haru with moveoutleft
    show erika
    e "What's up with - "
    show manami worried
    show erika isee
    e "Ohhh."
    stop music fadeout 2.0
    scene cg yukata 0
    with fade
    play sound "music/toiletdoor.ogg"
    h "..."
    h "Thank goodness the yukata are unisex..."
    h "I just hope that it's big enough for me..."
    scene cg yukata 1 with dissolve
    h "It looks like it should fit me fine."
    h "Yukata are all straight lines, so not having a waist or much of a chest is better..."
    h "So it's perfect for me... "
    h "I hope I can tie it well..."
    scene black with fade
    h "OK, that's not a good bow... Let me try that again."
    h "Maybe this is a little better?"
    scene cg yukata 2 with fade
    h "..."
    h "I'm OK with this."

    scene bg room
    show manami yukata at right
    show erika yukata at midright
    show haru yukata at left
    with fade
    play music "music/hotel.ogg" fadeout 2.0
    h "Sorry for the wait."
    show erika yukata grin
    e "Oh, looking pretty good!"
    show haru yukata blush
    h "Thanks."
    e "Yeah! If I didn't know better, I would've thought - "
    show haru yukata
    show erika yukata
    show manami yukata worried
    m "Erika!"
    m "I told you not to say..."
    h "It's OK."
    m "Haru..."
    show haru yukata tsuyoki
    h "It's better than the other possible reaction."
    h "Let's get going. I need to check the times for the reserved baths."
    e "What, you're not heading into the women's bath with us?"
    h "That would be a bit too... y'know."
    e "I don't think it'd be that big of a deal."
    m "Erika, don't..."
    h "It's fine! I want to check out the reserved baths anyway."
    h "Come on, let's go!"

    jump familybath

label familybath:
    show bg reception
    show haru yukata tsuyoki at left
    show erika yukata at right
    show manami yukata worried at midright
    with fade
    m "Haru, Erika and I are going to head in then..."
    h "You don't have to worry about me! I'll see you again at dinnertime."
    e "That's what she said, Manami. Let's go already."
    m "Ah, don't grab my arm - "
    show erika yukata grin
    e "See you later, Suzuki!"
    hide erika
    hide manami
    with moveoutright
    h "..."
    show haru yukata hmm
    h "I'm making Manami worry..."
    show haru yukata ganba
    h "I've got to stop that."
    show haru yukata
    h "First, I should find out how to reserve the bath..."
    h "Excuse me..."
    show bg reception lady
    f "How may I help you?"
    h "How do I book the reserved baths?"
    f "If you mean the family baths, please head to your left and write your name and room on the reservation list."
    h "...Thank you very much."
    h "..."
    f "The family baths are to your right."
    h "Yes, thank you!"
    hide haru with moveoutleft
    scene bg hall
    show haru yukata at left
    with fade
    h "I came here, but..."
    h "Is it really OK for someone like me to head into a family bath?"
    h "Can you even use family baths on your own?"
    h "I'd just be taking away a time slot from an actual family..."
    menu:
        h "What should I do...?"
        "Give up on the family bath":

            $ spoons -= 1
            show haru yukata down
            h "I can just take a shower back in my room."
            h "This way I won't cause trouble for anyone else..."
            h "It's a nice room too. I can relax until dinner."
            h "...No point in loitering here."
            jump rest
        "It's just one time slot...":

            show haru yukata hmm
            h "...I guess it should be OK if I don't take too long."
            h "It would be a shame if I came to a hot spring but didn't actually go in..."
            h "And it's been so long since I've been at a proper one..."
            show haru yukata ganba
            h "OK. I'm going to reserve a time slot."
            h "Let's see..."
            show haru yukata hmm
            h "..."
            h "......"
            h "........."
            h "They're all booked."
            h "Are you serious?"
            h "And here I was trying so hard to encourage myself..."
            show haru yukata down
            h "..."
            q "Excuse me..."
            show haru yukata panicked
            h "Sorry I was just leaving!"
            show staff at right with easeinright
            s "Would you like to book the family baths?"
            show haru yukata
            h "Er... I was going to, but they're all booked."
            show staff surprised
            s "Oh no! I sincerely apologise for the inconvenience."
            show staff
            s "May I suggest you enjoy our splendid women's baths instead?"
            s "We have vase-shaped bathtubs which you can enjoy privately, like the family baths."
            show haru yukata down
            h "..."
            s "If you would like, I can show you to the baths."
            show haru yukata panicked
            h "No!"
            show staff surprised
            s "Is something the matter?"
            h "No, I just..."

            menu:
                h "I..."
                "Tell her it's nothing":
                    $ spoons -= 1
                    show haru yukata tsuyoki
                    h "It's nothing. I know where the baths are, so I'll be fine."
                    show staff bow
                    s "Is that so! Then, I hope you enjoy your stay."
                    hide staff with moveoutright
                    h "..."
                    show haru yukata down
                    h "I guess I'll head back to my room."

                    jump rest
                "Give an explanation":
                    $ rotenburo = 1
                    h "The truth is..."
                    h "I think that if I go into the women's baths, it might make the other patrons uncomfortable..."
                    h "That's why I wanted to use the family baths."
                    show staff surprised
                    s "I see..."
                    s "I understand your concerns."
                    s "However, as it is, you won't be able to enjoy the baths in this wonderful hot spring town..."
                    s "I can't allow that."
                    h "What?"
                    s "I can't allow one of our guests to miss out our fantastic hot springs!"
                    h "No, it's my own problem, so -"
                    show staff
                    s "No. You came to enjoy the hot springs, so I will ensure that you can."
                    s "Would you please tell me your name and room?"
                    h "Er, it's Haru... Haruto Suzuki in the Gingko Room."
                    show staff surprised
                    s "That would be... Mr Haruto Suzuki then?"
                    h "...Ms would be fine."
                    show staff bow
                    s "Please forgive me. Now, if you would please wait here for a moment..."
                    hide staff with moveoutright
                    show haru yukata hmm
                    h "...Now I'm even causing trouble for the staff."
                    h "I guess I should just wait."
                    show staff bow at right with easeinright
                    s "I apologise for the wait."
                    show haru yukata
                    h "No, that was hardly any wait at all!"
                    show staff
                    s "With your permission, we would like to upgrade your party to a room with an open-air bath."
                    h "What?!"
                    s "Would that be acceptable?"
                    h "I don't want to cause any fuss..."
                    s "It is our way of apologising for the fully booked family baths."
                    s "We want all of our guests to enjoy our hot springs."
                    s "It's also a personal wish from a staff member who loves this hot spring town."
                    s "Will you accept the upgrade?"
                    h "I..."
                    h "Is it really OK?"
                    s "Of course!"
                    h "Then..."
                    show haru yukata blush
                    h "Yes, please."
                    s "Thank you very much! If you would allow me to accompany you to your room..."
                    jump rotenburo

label rotenburo:
    scene bg room
    show haru yukata blush at left
    show staff at right
    with fade
    s "This is the Azalea Room."
    h "I don't know how to thank you..."
    show staff bow
    s "It was nothing! I hope you enjoy your stay."
    hide staff with moveoutright
    h "What a nice person..."
    h "She said she would tell Manami and Nagata about the change in rooms too."
    h "I didn't think people would be that accommodating."
    h "...Maybe the world is kinder than I thought it was."
    show haru yukata
    h "Let's check out the open-air bath then..."
    scene bg rotenburo
    show haru yukata hmm at left
    with fade
    h "...This is really, really nice."
    h "The view is amazing..."
    h "I don't even want to think about how much it would cost normally."
    h "It's absolutely gorgeous..."
    h "Is it really OK to get an upgrade like this for free?"
    show haru yukata ganba
    h "Ack, stop worrying, Haru."
    h "The staff said it was OK, so I'm going to enjoy this."
    h "I need to wash first..."
    stop music fadeout 2.0
    scene black with fade
    play sound "music/shampoo.ogg"
    h "Oh, I love the smell of this shampoo... Chrysanthemum?"
    h "It's really relaxing..."
    play sound "music/putdown.ogg"
    h "And this is a... charcoal soap? Cool."
    h "Now to try out the conditioner..."
    play sound "music/wash.ogg"
    h "And now to wash it all off..."
    h "And head into the bath."
    scene cg rotenburo 0
    with fade
    play music "music/onsen.ogg" fadeout 2.0
    h "Oh, wow..."
    h "I can feel the knots in my muscles loosening..."
    h "I can't even remember how long it's been since I've soaked in real hot spring water..."
    h "I could never afford to go to a place like this myself..."
    h "And I can't go into the regular hot springs..."
    h "All I've got is my bathtub at home..."
    scene cg rotenburo 1 with dissolve
    h "I wish I could stay in here forever..."
    scene black with fade
    h "..."
    h "......"
    h "........."
    scene cg rotenburo 1 with fade
    h "Ahh, that was a good soak."
    h "I should get dressed..."
    h "What a wonderful bath."
    h "Thank you, staff lady..."
    stop music fadeout 2.0
    jump dinner

label rest:
    scene bg room
    show haru yukata at left
    with fade
    h "I have a couple of hours before dinnertime."
    h "Manami and Nagata probably won't be back for a while either."

    menu:
        h "How should I pass the time?"

        "Take a shower" if spoons >= 2:
            $ shower = 1
            h "I still need to wash even if I don't head into the hot springs."
            h "Luckily, the room comes with a shower."
            h "I know some places only have showers by the hot springs."
            h "Let's see what kind of products they have."
            stop music fadeout 2.0
            scene black with fade
            h "So they have shampoo, conditioner, and soap..."
            h "I'm happy they have separate shampoo and conditioner. The combined ones aren't great."
            play sound "music/shampoo.ogg"
            h "The shampoo smells nice..."
            h "Same for the conditioner..."
            play sound "music/putdown.ogg"
            h "Charcoal body soap? I guess it's pretty popular lately."
            play sound "music/wash.ogg"
            h "And now to wash it all off..."
            h "That was a nice refreshing shower."
            h "Let's head back to the room."
        "Get in a quick nap":

            h "Maybe I'll get in a quick nap."
            h "I'm already kind of tired..."
            stop music fadeout 2.0
            scene black with fade
            h "The futon is out already, but the tatami is nice..."
            h "I'll just... take a quick... nap..."

    jump dinner

label dinner:

    scene bg room
    show haru yukata at left
    with fade
    play music "music/hotel.ogg" fadeout 2.0


    h "Wow, time passed pretty quickly."
    h "Manami and Nagata should be back soon."

    show manami yukata at right
    show erika yukata at midright
    with easeinright

    m "We're back!"
    e "Hey, Suzuki."

    if rotenburo == 1:
        m "I heard from the staff that we were upgraded to a room with an open-air bath!"
        h "Yeah, because the family baths were all booked."
        show manami yukata hehe
        m "Wow! That's so nice of them!"
        e "The staff didn't just tell you to go to the women's baths?"
        show manami yukata worried
        m "Erika!"
        menu:
            h "..."
            "Reply honestly":

                $ reply = 1
                h "She did, but when I explained, she was very understanding."
                e "Whoa, that's really cool of her!"
                show haru yukata blush
                h "Yeah..."
                h "I was surprised, but really happy."
            "Say nothing":


                $ spoons -= 1
                h "..."
                m "Erika, why would you - "
                show haru yukata down
                h "It's fine."
                m "Haru..."
    else:
        m "Did you enjoy the reserved baths?"
        menu:
            h "(I didn't go in... What should I say?)"
            "They were great!":

                $ lie = 1
                $ spoons -= 1
                show haru yukata tsuyoki
                h "They were great! It was really relaxing."
                m "Oh, that's wonderful!"
            "I didn't go in...":
                show haru yukata down
                h "Actually, I didn't go in..."
                show manami yukata worried
                m "Why not?"
                h "They were all booked..."
                m "Oh no...! I'll go check if there's anyway they could open it up, just for a little."
                m "It would be such a waste if you couldn't go in at all."
                show haru yukata tsuyoki
                h "It's fine!"
                if shower == 1:
                    h "I took a shower and get all refreshed."
                    h "It was really relaxing."
                    m "Are you sure...?"
                    h "Yup!"
                else:
                    h "I was feeling tired anyway, so I took a nap."
                    m "OK then..."
                    h "I'm fine, Manami."
    show haru yukata
    h "Did you two enjoy the hot springs?"
    show manami yukata
    m "Yup! It was really nice."
    show erika yukata grin
    e "Yeah, I've never been to such a proper expensive place before."
    e "You should've come with us!"
    h "Haha, I'm glad you enjoyed it."
    m "Oh, Haru, I think you've got something in your hair."
    show manami yukata at midleft with ease
    m "Let me get that for you - "
    show haru yukata blush
    h "It's OK! I'll get it myself!"
    m "You don't even know where it is!"
    h "You can tell me!"
    m "But it would be easier if I took it."
    m "There, I got it."
    h "Thanks..."
    show erika yukata isee
    e "Hmm. Is that how it is?"
    m "Is what how it is?"
    show erika yukata grin
    e "Nothing, nothing."
    show erika yukata
    e "When is dinner getting here?"

    play sound "music/knock.ogg"

    "*knock*"
    q "Excuse me."
    show staff at right with easeinright
    s "Good evening. Please allow me to set the table for you."
    s "What would you like to drink?"
    m "What do you two want?"
    h "Er..."
    show erika yukata grin
    e "How about beer for everyone?"
    h "I'm underage so I'll just have oolong tea."
    e "Right, right."
    e "Two beers and one oolong tea, please!"
    show staff bow
    s "Please enjoy your meal."
    hide staff with moveoutright
    play sound "music/hikidoclose.ogg"

    show haru yukata
    h "Manami, are you OK with beer?"
    show manami yukata worried
    m "I've never actually drunk before..."
    e "It'll be fine! It's your 20th, so you should try a bit at least."
    e "If you don't like it, I'll drink it for you."
    e "More importantly, this dinner!"
    h "This looks..."
    e "Amazing?!"
    m "Let's eat!"

    scene cg dinner 0 with fade
    m "I requested a tofu nabe so that we can all share!"
    m "Don't worry, Erika - it's all vegetarian."
    h "You're vegetarian, Nagata?"
    e "Yeah, so it's really tough eating out."
    e "I can't even get a salad without worrying about it having animal products inside."
    h "Really? Isn't it just vegetables?"
    m "Haha, you'd be surprised! There's stuff like bacon and gelatin sometimes."
    e "Yeah, Manami bought me a potato salad with gelatin and bacon before."
    m "But I know better now!"
    m "Anyway, the drinks are here, so we should toast."
    e "You're the birthday girl, so go ahead!"
    m "OK then..."
    m "Thank you for celebrating my birthday with me."
    m "It means a lot to me to have my two best friends here!"
    m "A toast to my friends!"
    scene cg dinner 1 with dissolve
    play sound "music/kanpai.ogg"
    m "Cheers!"
    he "Cheers!"
    e "Now that we've got that over with..."
    hme "Let's eat!"
    scene black with fade
    stop music fadeout 2.0
    h "This tempura maitake is so crispy..."
    e "Oh man, this tofu is so soft!"
    m "It tastes even better with a bit of the pink salt."
    scene cg dinner 2 with fade
    play music "music/hotel.ogg" fadeout 2.0
    hme "That was delicious!"
    h "I'm so... full..."
    e "Of course you are! How many bowls of rice was that?"
    h "I don't know..."
    m "I'm... at my limit... too..."
    e "You two are idiots."
    m "Haru isn't... an idiot..."
    h "Neither is Manami..."
    e "Such idiots."
    m "My body feels... really heavy..."
    m "...zzz..."
    e "Ah, she fell asleep..."
    e "Suzuki, can you help me carry her to the futon?"
    h "Ah... OK."

    jump afterdinner

label afterdinner:

    scene bg room
    show haru yukata at left
    show erika yukata at right
    with fade
    e "She's surprisingly heavy."
    h "Because she does sports. It's the muscle."
    show erika yukata isee
    e "Really? I didn't know that."
    e "Though I can imagine it."
    e "She's always so full of energy."
    e "She went out like a light today though."
    show haru yukata hmm
    h "I think it was the beer."
    show erika yukata
    e "Yeah... Trust Manami to be such a lightweight."
    e "It's a good opportunity for me though."
    show haru yukata
    h "A good opportunity?"
    e "I wanted to talk with you!"
    e "But Manami was being all sensitive about it."
    e "So I figured I'd ask when Manami wasn't around."
    e "I'm not great with this sort of thing, to be honest."
    e "But I really just want to understand a bit better."
    e "And you can tell me to stop at any time if you don't want to talk, so..."
    e "Mind if we chat for a bit?"

    h "(Nagata is Manami's friend, so I'm sure she really does just have good intentions...)"
    h "(But I haven't really properly talked about this to anyone before...)"
    menu:
        h "(What should I tell her...?)"
        "I'm a bit tired, so...":

            h "Sorry, I'm a bit tired, so..."
            show erika yukata isee
            e "Oh, OK then."
            e "Sorry for asking something weird!"
            if rotenburo == 1:
                e "I'm gonna take a dip in the open-air bath then."
            else:
                e "I'm gonna take another dip in the baths then."
            e "Don't wait up!"
            hide erika with moveoutright
            show haru yukata down
            h "..."
            h "I must have disappointed Nagata."
            h "But I'm not really up for talking about being transgender today."
            h "Especially not with Manami's friend..."
            h "I haven't even really talked about it properly to Manami yet."
            h "She always just waves it off, saying that it doesn't matter."
            h "But it matters to me... It's who I am."
            h "..."
            h "It's too early to sleep, so maybe I'll just rest for a bit."

            jump hiroen

        "What do you want to talk about?" if spoons >= 1:
            $ talk = 1
            h "...What do you want to talk about?"
            show erika yukata grin
            e "You don't have to get so prickly!"
            e "I'm just a bit curious since you're the first transgender person I've ever met."
            show haru yukata hmm
            h "That might not be true."
            show erika yukata
            e "Huh?"
            h "You might have met other transgender people before, but you just didn't notice."
            show erika yukata isee
            e "Maybe... To be honest, if Manami hadn't told me, I wouldn't have known you were transgender, Suzuki."
            show erika yukata
            e "Can I just call you Haru? You can call me Erika."
            show haru yukata
            h "I don't mind."
            e "Haru then. Is that like, your transgender name?"
            show haru yukata hmm
            h "Er, no... It's a nickname from when I was a kid."
            e "Oh, so a nickname from when you were still a guy?"
            menu:
                h "(...How should I respond?)"
                "I wasn't a guy before...":
                    h "..."
                    h "It's not like I was a guy before... I've always been a girl."
                    h "Just my appearance doesn't completely match who I am..."
                    e "Sorry, I shouldn't have phrased it that way."
                "It's from my legal name...":
                    $ spoons -= 1
                    h "It comes from the name on my family register."
            e "What was your name again? I heard it at check-in. Haruto, right?"
            h "...You probably shouldn't ask that sort of thing to transgender people."
            e "Why?"
            h "Asking for a name someone isn't using now is kind of like denying who they are now, so..."
            show erika yukata isee
            e "Oh... Sorry about that! I didn't mean it that way, so could you forget it?"
            show haru yukata
            h "It's OK. I actually like the name Haru. It's unisex."
            h "I'd like to change my legal name to Haru if I can."
            e "Oh, I guess since you haven't changed your name, you can't use Haru on official documents and stuff."
            h "Yup..."
            e "I guess your legal gender is still..."
            h "Yup."
            e "It must be hard on you."
            e "Can't you change it?"
            h "It's a bit tough."
            h "I would need to get gender affirmation surgery and be sterilized..."
            show erika yukata
            e "What? I mean I guess gender affirmation surgery is cool if you want to change your body anyway -"
            e "But you need to be sterilized?!"
            h "Yeah. Though in some other countries, you can change your gender without doing either."
            show erika yukata isee
            e "I didn't know..."
            show haru yukata down
            h "Yeah, there are a lot of requirements..."
            h "You also have to be above 20, not married currently, and have no kids who are minors."
            e "Wait, why do you have to be unmarried and not have kids?"
            h "Well, for the marriage bit... Because if you changed gender, it'd become a same-sex marriage."
            h "And that's illegal in Japan..."
            h "And for the children bit, apparently it would be confusing for them or something."
            e "What the hell!"
            h "I know. I didn't make the law."
            h "It might get better though... Some wards allow same-sex partnership now, after all."
            e "I didn't realise it was so bad..."
            e "...I'm sorry for asking you so many questions."
            e "I hope I didn't make you uncomfortable."

            menu:
                h "(What should I say?)"
                "Thank Erika for listening":
                    show haru yukata blush
                    h "It's fine... I'm actually happy."
                    h "Thank you for listening."
                    show erika yukata
                    e "Thank you for sharing with me!"
                "Tell Erika it's OK":

                    show haru yukata tsuyoki
                    h "It's OK. I'm used to it."
                    e "Sorry... I just asked 'cause I was curious."
                    e "I didn't really think too much about it."
                    h "It's fine."

            show erika yukata grin
            e "OK. I think that after I made you spill out all of that, I definitely owe you one."
            show haru yukata
            h "Huh?"
            e "I talked to one of the attendants earlier."
            e "Apparently, while their official stance is that you should enter the baths for your legal gender..."
            e "This is a question they're actually asked quite often."
            e "And they decided that it was unofficially OK, as long as you didn't bother other guests."
            e "There aren't too many guests today, since it's a weekday."
            e "And she said that the bath would probably be empty around midnight."
            h "...So?"
            e "So nobody would have a problem if you went into the women's baths. Because nobody would be there."
            show haru yukata panicked
            h "I can't just go in!"
            e "Calm down! It'll be fine."
            h "But what if somebody's there?"
            e "The baths are big. We'll just keep away from them."
            h "But what if they look?!"
            e "They won't look - and even if they do, who cares!"
            e "If anybody says anything, I'll beat them up!"
            h "Please don't beat them up...!"
            e "It'll be fine!"
            h "But - but you were drinking earlier!"
            e "That was hours ago! It's out of my system now."
            show haru yukata
            show erika yukata
            e "Come on, Haru. Don't you want to enter the women's baths?"
            e "You're a woman too. You have the right."
            h "Erika..."

            menu:
                h "(What should I do?)"

                "Go to the baths" if spoons >= 1:

                    show haru yukata hmm
                    h "..."
                    h "OK, I'll go. But if anything happens -"
                    show erika yukata grin
                    e "It'll be fine!"
                    show erika yukata grin at midleft with ease
                    e "Let's grab our towels and go."
                    show haru yukata blush
                    h "Wait -"
                    e "Come on!"
                    hide erika
                    hide haru
                    with moveoutleft

                    jump womensbath
                "Don't go to the baths":

                    show haru yukata down
                    h "Sorry... I just can't."
                    h "I'm still a male legally... I don't feel like it's OK for me to go into a female space."
                    e "But that's just legally, right?"
                    e "Transgender means that even if you have a guy's body, you're still really a girl, right?"
                    h "Yes, but..."
                    h "Sorry, Erika. I just can't."
                    h "Go without me."
                    show erika yukata isee
                    e "Fine, I won't push it."
                    e "I'll probably take a while, so head to sleep first, OK?"
                    hide erika with moveoutright

                    h "..."
                    h "It's pretty late. I should get to sleep."
                    stop music fadeout 2.0
                    jump morning

label womensbath:
    $ womensbath = 1
    scene bg hall
    show haru yukata down at left
    show erika yukata at right
    with fade
    play music "music/hotel.ogg" fadeout 2.0
    h "Actually, I think I'll - "
    e "Come on. You've made it all the way here already."
    e "I'll even check to make sure nobody else is inside."
    hide erika with moveoutleft
    h "..."
    show erika yukata grin at midleft with easeinleft
    e "All the keys are in the lockers."
    e "Nobody's in the hot springs."
    e "Come with me?"
    h "..."
    show haru yukata
    h "OK."
    hide erika
    hide haru
    with moveoutleft
    stop music fadeout 2.0
    scene black with fade
    e "Don't worry, I'll change over here."
    e "I won't look or anything."
    h "Thanks..."
    e "You can head in first to wash!"
    h "See you later then..."
    play sound "music/onsendon.ogg"
    scene cg womensbath 0 with fade
    play music "music/onsen.ogg" fadeout 2.0
    h "Wow..."
    h "It's so nice in here..."
    if rotenburo == 1:
        h "The water feels smoother than the one in the room somehow."
    else:
        h "The water feels so smooth..."
    scene cg womensbath 1 with dissolve
    e "That's because it's got a lot of minerals in it that are good for your skin. "
    e "What do you think? Pretty good, right?"
    h "Yeah..."
    h "Thanks for bringing me."
    e "I don't see what the big deal is."
    e "I don't understand why you didn't just come into the bath with Manami and me."
    h "You don't get it."
    e "What don't I get?"
    h "Hmm..."
    menu:
        h "Let's pretend for a moment that you're in..."
        "A school lavatory":
            h "A school lavatory. There's one for girls and one for boys. Which one do you go into?"
            e "The one for girls, of course."
            h "Of course."
            h "What if a student in a male uniform came into the washroom then?"
            e "Well, I guess I'd tell them they were in the wrong washroom."
            h "Of course."
            h "But what if they said they were in the right one?"
            e "I'd probably have called a teacher."
        "Gym class":

            h "Gym class, in high school. You need to change into your gym uniform."
            h "Girls change in the changing room. Boys change in the classroom."
            h "Where do you change?"
            e "I'd go to the changing room with the rest of the girls."
            h "Of course you would."
            h "What if one of the boys tried to come with you?"
            e "...We'd probably all call him a pervert."
            e "But I mean, you look like a girl, Haru."
            h "But I'm not. At least, not physically. Not completely."
            h "...And a lot of people aren't as lucky with the appearance as me."
    e "..."
    h "..."
    e "This isn't just pretend, is it..."
    e "You're speaking from experience, aren't you?"
    h "..."
    e "..."
    h "People like you know exactly where you belong."
    h "But people like me don't \"belong\" anywhere."
    h "We can't just enter bathrooms or changerooms or hot springs."
    h "If I went into a men's bathroom like this and was seen, I'd be told I was in the wrong washroom."
    h "But society tells me I can't use the women's bathroom either."
    h "It's the same for the hot springs, so we have to watch out for ourselves."
    h "...Since nobody else will."
    h "Even though we just want to live like everyone else..."
    e "..."
    e "It must have been really tough for you in high school."
    h "...My school wouldn't allow boys to wear anything but the male uniform."
    h "But I didn't act like how they thought a boy should act."
    h "I got called a lot of names because of that..."
    scene cg womensbath 3 with dissolve
    e "Yeah, high school students can be vicious."
    e "I was at an all-girls school, but things got pretty bad sometimes."
    h "Manami never said anything like that."
    e "Well, yeah. She's Manami. Nothing bad ever happens around her."
    e "But I was a bit of a delinquent."
    h "A bit of a delinquent...?"
    e "Wearing my uniform wrong. Fighting with bullies. Smoking in the toilets."
    e "Y'know. The usual."
    h "Er, I don't know how \"usual\" that is..."
    e "Well I've got over that rebellious phase now."
    e "But I know kids can be pretty awful."
    e "Girls' bullying isn't as obvious as cuts and bruises, but it sticks with you."
    h "...Were you bullied too?"
    e "It wasn't that bad."
    e "I didn't fit in."
    e "Manami was pretty much my only friend in high school, and we weren't even in the same class."
    e "My homeroom teacher said it was my fault for not trying to be nice, so I just stopped caring."
    h "That's awful..."
    e "Right? But that's just how things are in high school."
    e "The people who don't fit in will never fit in."
    e "So it's better to just stop caring and enjoy yourself."
    e "With people who don't mind that you're different."
    h "Yeah..."
    scene cg womensbath 1 with dissolve
    e "Sorry for that incredibly depressing speech."
    h "No, no - I'm really happy you shared that with me."
    h "I don't know why, but I feel like somebody's lifted the weight off my shoulders."
    e "Haha, then I'm glad I talked to you."
    e "Have you ever told Manami any of this?"
    h "No..."
    h "I could never tell her. She's done so much for me..."
    h "It would just make her sad if she knew..."
    e "..."
    e "Oh wait, I'm sure of this now."
    e "You like Manami, don't you?"
    stop music fadeout 2.0
    menu:
        h "..."
        "...":
            h "..."
            e "You don't have to say anything."
        "Yeah...":
            h "..."
            h "Yeah..."
    e "You know that she's... You know, right?"
    h "Yeah, I know."
    h "She talks about her boyfriend a lot."
    h "He sounds like a really nice guy."
    play music "music/onsen.ogg" fadeout 2.0
    scene cg womensbath 2 with dissolve
    h "..."
    e "..."
    e "I mean, I don't think there's any problem with that, OK?"
    e "I dated a girl before too."
    scene cg womensbath 1 with dissolve
    h "Really?"
    e "Yeah, back when I was in high school. I dated somebody at my part-time job."
    h "So you're bi then?"
    e "Bi?"
    h "That you like both men and women."
    e "Maybe. To be honest, I don't really know. I don't care much for labels."
    e "But it's cool. You do you."
    e "Want to check out another bath? They've got a nice hot one in cypress wood."
    h "Sure!"
    scene black with fade
    e "It's kinda cute how you hide your chest with your towel, by the way."
    h "I thought you said you wouldn't look!"
    e "Sorry! I didn't mean to."
    e "But you do look cute."
    h "...OK, I'm heading into one of the vase tubs by myself."
    stop music fadeout 2.0
    e "Oh, come on!"

    scene bg hall
    show haru yukata at left
    show erika yukata at right
    with fade
    play music "music/hotel.ogg" fadeout 2.0
    e "Ah, that was great! Hot springs are the best at night when it's quiet."
    h "Yeah..."
    show haru yukata blush
    h "Thank you for bringing me."
    e "Haha. Like I said, it's not a big deal."
    e "I'm gonna grab a drink. What do you want?"
    show haru yukata
    h "Oh, it's OK. I'm fine."
    e "Then I'll just choose for you. Wait here for a bit."
    hide erika with moveoutright
    h "Erika's... an interesting person."
    h "But nice."
    h "I guess I should wait here..."
    if rotenburo == 1:
        show staff at right with easeinright
        s "Oh! Good evening. It was... Miss Suzuki, yes?"
        s "Did you perhaps have a chance to enjoy the women's baths?"
        show haru yukata panicked
        menu:
            h "(How should I respond?!)"
            "Yes...":

                $ yes = 1
                h "Yes..."
                h "But only because I knew there was nobody else inside."
                h "But I wasn't the one that checked! My friend looked in the changing room for me, so..."
                s "Ah, yes. The baths are usually empty at this hour."
                s "It isn't uncommon for people who want to bathe alone to use the baths at this time."
                show staff bow
                s "So I am very pleased to hear that you could enjoy the baths."
            "No!":
                h "No! I didn't go in!"
                h "It's fine!"
                show staff surprised
                s "Is that so..."
                s "It actually isn't uncommon for people who want to bathe alone to use the baths at this time."
                s "People who may be concerned about others looking at them, for example."
                show staff bow
                s "The baths are still open, so please feel free to use them."
        s "I hope you have a pleasant night."
        hide staff with moveoutright
        show haru yukata
        h "..."
        h "She knows, doesn't she..."
        h "But she didn't say anything..."
        h "She pretty much said it was OK for me to go into the women's baths..."
        show haru yukata blush
        h "..."
        h "I'm... really happy..."
    show erika yukata grin at right with easeinright
    e "Hey! Got you some herb tea."
    show haru yukata
    h "Thanks."
    show haru yukata blush
    h "...It tastes good."
    e "Right?"
    e "When you're done drinking that, let's head back to our room."
    h "OK."
    jump backtoroom

label backtoroom:

    scene bg room
    show erika yukata at right
    show haru yukata at left
    with fade
    e "OK, I'm tired as hell, so I'll see you in the morning."
    e "Night!"
    h "Good night."
    hide erika with moveoutright
    h "I should get to sleep too..."
    h "..."
    show haru yukata blush
    h "I think I'll have good dreams tonight."
    stop music fadeout 2.0
    jump morning

label hiroen:

    h "...This kind of reminds me of my school trip."
    h "I wasn't friends with anyone in my group."
    h "I spent all of my free time just hiding from everyone else."
    h "At school I had to wear the boy's uniform, so of course I was in a group of all boys too..."
    h "An hour in the hot springs at the hotel was on the itinerary, so of course there was no opting out."
    h "I had stopped going to public baths ever since I was too old to go into the women's bath with my mum..."
    h "Even at that age, I wouldn't even consider heading into the men's bath."
    h "But the teacher tried to make me go into the men's bath with everyone else."
    h "I just hid in the changing room toilet the whole time."
    h "..."
    if rotenburo == 1:
        show haru yukata
        h "I got to go into the hot spring this time though."
        h "Even if it was just the one in the room."
    else:

        h "I didn't end up going into the hot spring this time either..."
    show haru yukata hmm
    h "This trip is definitely better overall."
    h "I mean, nobody's ignoring me or calling me names, so..."
    q "Haru?"
    show haru yukata panicked
    show manami yukata surprised at right with easeinright
    h "Manami?!"
    m "What are you doing still up?"
    h "(Did Manami hear me talking to myself?!)"
    h "I was just about to head to bed."
    show manami yukata
    m "Oh! Then I won't bother you."
    show haru yukata
    h "..."
    h "(Looks like she didn't hear.)"
    h "You aren't heading back to sleep?"
    m "I think I'm just going to stay here for a bit."
    m "I fell asleep right after dinner, so I haven't had a chance to really enjoy the room."
    m "I won't keep you if you're tired, but..."
    m "If you don't want to sleep yet, won't you stay up a bit later and keep me company?"
    menu:
        h "..."
        "Head to sleep":

            show haru yukata down
            h "Sorry, I'm a bit exhausted."
            show manami yukata worried
            m "Are you OK?"
            show haru yukata tsuyoki
            h "Yup! It's just been a long day."
            m "..."
            m "If you say so."
            show manami yukata
            m "I'm going to head out to get something to drink."
            m "Good night!"
            hide manami with moveoutright
            h "..."
            show haru yukata down
            h "Sorry, Manami..."
            h "I'm just not up for a conversation right now..."
            h "...I should get some sleep."

        "Keep Manami company" if spoons >= 1:
            $ hiroen = 1
            h "I can stay up for a little bit longer."
            show manami yukata hehe
            m "Yay!"
            m "Let's head over to the window."
            stop music fadeout 2.0
            scene cg hiroen 1
            with fade
            play music "music/hiroen.ogg" fadeout 2.0
            m "The moon is really beautiful tonight."
            h "It really is..."
            m "I love how quiet it is out here."
            m "It's like the whole world is asleep."
            h "Yeah..."
            m "It's too bad you didn't get to enter the big baths..."
            if lie == 1:
                $ spoons -= 1
                m "But I'm glad you got to enjoy the reserved baths!"
                h "..."
                m "Haru?"
                h "Ah, yeah, the reserved baths were really nice!"
            else:
                if rotenburo == 1:
                    m "Even if we did get upgraded to a room with an attached bath."
                menu:
                    h "It's OK! I'm happy I got to..."
                    "Stay in this beautiful ryokan":

                        $ spoons -= 1
                        h "I got to stay in this beautiful ryokan."
                        h "Normally, I'd never go to a place like this."
                        m "But still..."
                    "Be here for your birthday":
                        h "I got to be here with you to celebrate your birthday."
                        h "That's enough for me."
                        m "Haru..."
                h "It's fine, Manami. Thanks for inviting me."
            h "It's been a good trip."
            m "It isn't over yet!"
            m "But it's kind of strange to think that I'm officially an adult now..."
            h "(Right... Once the clock turns 12, Manami's birthday will be over...)"
            h "(I got her a present, but...)"
            menu:
                h "(I don't know if it's really OK to give it to her...)"

                "Give Manami the present" if spoons >= 1:
                    $ present = 1
                    h "..."
                    m "Haru? You OK?"
                    h "Actually... I got you a present."
                    m "Wow, really? Thank you!"
                    h "But... I don't have it on me right now."
                    h "Could I give it to you in the morning?"
                    m "Oh, of course!"
                    h "Then... tomorrow."
                    h "I think I'm going to head to bed."
                    m "Hey, Haru..."
                    m "You know you can tell me anything, right?"
                    m "Anything."
                    h "Haha, what's up with you?"
                    m "Nothing, but I just..."
                    h "You don't have to worry about me."
                    h "Good night!"
                    m "Good night..."
                    scene cg hiroen 2
                    with dissolve
                    m "..."
                    m "I wish you'd be more honest with me, Haru..."
                "Just wish Manami a happy birthday":

                    h "..."
                    m "What is it?"
                    h "Oh, I was just thinking that I hadn't said this yet."
                    h "Happy birthday, Manami."
                    m "Thanks, Haru."
                    m "It's kind of funny, isn't it?"
                    m "We've been together since we were children, and soon we'll both be adults."
                    m "We've grown up, haven't we?"
                    h "Yeah..."
                    m "But nothing's changed."
                    m "That makes me really happy."
                    h "..."
                    m "You'll always be my oldest and my best friend, Haru."
                    m "Thanks for being here with me."
                    h "Yeah, of course. Always."
                    m "You really have to meet my boyfriend sometime!"
                    m "He's always saying that he wants to meet you since I talk to you so much."
                    h "Yeah, sometime."
                    m "How about we all go out for dinner?"
                    h "I'd have to check my schedule..."
                    m "Oh, of course!"
                    m "Just let me know whenever you're free and we'll make time."
                    m "I can't wait. I think you'll really like him."
                    h "I'm sure I will. He's your boyfriend."
                    m "Hehe."
                    m "Ah, I'm feeling a bit sleepy again..."
                    m "I think I'll go back to bed."
                    m "How about you?"
                    h "I think I'll enjoy the view for a little bit longer."
                    m "OK then! Good night."
                    h "Good night."
                    scene cg hiroen 0
                    with dissolve
                    h "..."
                    h "Manami's boyfriend, huh..."
                    h "I'm sure he got her a wonderful present."
                    h "...A present from me would probably just be a bother."
                    h "..."
                    h "I think I'll go to sleep too..."
                    h "...Just a bit later."

    stop music fadeout 2.0
    jump morning

label morning:

    scene bg room
    show haru yukata at left
    with fade

    play music "music/morning.ogg"

    h "...It's morning."

    if womensbath == 1:
        jump erikaend2
    elif talk == 1:
        jump erikaend1
    elif present == 1:
        jump manamiend2
    elif hiroen == 1:
        jump manamiend1
    elif spoons >= 1:
        jump normalend
    else:
        jump badend

label erikaend1:
    show manami surprised at right with easeinright
    m "Good morning! You're finally awake?"
    m "I thought you two would never wake up!"
    h "You two?"
    show manami
    m "Erika's still asleep."
    show manami at midright with ease
    show erika yukata isee at right with easeinright
    e "Talking about me behind my back?"
    e "That's so mean of you, Manami."
    show manami surprised
    m "No, I was just saying -"
    show erika yukata grin
    e "I'm just kidding."
    show manami
    e "Morning, you two."
    h "Good morning."
    e "I guess it's time to check out?"
    show manami worried
    m "It is... You two missed breakfast."
    show haru yukata hmm
    h "It's OK, I'm not that hungry anyway."
    show erika yukata
    e "Speak for yourself! I want breakfast."
    show manami hehe
    m "I thought you might say that!"
    m "So actually, I got an attendant to pack one breakfast bento for each of us."
    m "I'll check us out, so while I'm doing that, you two should get dressed."
    m "I'll wait for you in the lobby!"
    hide manami with moveoutright
    show erika yukata isee
    e "I will never understand how she can be so energetic in the morning."
    show haru yukata
    h "Me neither."
    show erika yukata
    e "I guess we should get changed."
    h "Yeah."
    e "Oh, but before you go..."
    h "Hm?"
    show erika yukata isee
    e "Sorry."
    h "What for?"
    e "I was kind of insensitive this whole trip."
    e "I didn't mean to be, but I know I made you feel uncomfortable."
    e "But I think I know a little bit better now."
    e "Would you forgive me?"
    menu:
        h "(What should I say?)"
        "Of course":

            pass
        "There's nothing to forgive":
            show haru yukata tsuyoki
            h "There's nothing to forgive."
            e "Don't say that."
            e "Like, it's obvious you were hurt by it."
            e "But you just keep hiding it."
            e "You're just hurting yourself more, y'know?"
            show haru yukata down
            h "..."
            show erika yukata grin
            e "It's easier to just be honest!"
            e "So I'll ask once more."
            e "Would you forgive me?"
            menu:
                h "..."
                "Of course":

                    pass
    show haru yukata blush
    h "Of course I do."
    h "You listened to me."
    h "...Not everyone does."
    show erika yukata
    e "Great!"
    e "Let's get changed then. Don't want to keep Manami waiting."
    h "Right, we should hurry."

    scene bg reception
    show haru at left
    show manami worried at midright
    show erika at right
    with fade

    m "Finally! What took you two so long?"

    show erika grin
    e "Oh come on, it wasn't that long."
    e "Where are those breakfasts you mentioned?"

    show manami hehe
    m "Right here!"
    m "I didn't eat breakfast yet either, so we can eat them together on the train ride back."
    h "Oh, I..."
    h "(I planned on taking a different train, like when I came here...)"

    e "What, don't tell me you're going on a different train?"
    e "We're all headed in the same direction, right?"
    e "Let's head back together!"
    show manami
    m "I want to head back together too!"
    m "I still have lots I want to talk about."

    h "..."
    show haru blush
    h "...Me too."
    e "So, it's decided then."
    show manami hehe
    m "Yay! Let's go!"

label erika1:
    $ _skipping = False
    $ quick_menu = False
    scene cg erikaend1
    with fade

    show text "{font=tl/None/npckc.ttf}ERIKA END 1)\nNEW FRIEND, NEW ADVENTURES{/font}" at credits with Dissolve(1.5)
    pause
    hide text with dissolve
    show text "{font=tl/None/npckc.ttf}CREDITS\nStory/Code/Art: npckc\nMusic: maxdotine & npckc\nSE: Pocket Sound\n\nThank you for playing!{/font}" at credits with Dissolve(1.5)
    pause
    stop music fadeout 3.0
    scene black with Dissolve(3.0)
    $ _skipping = True
    $ persistent.erika1 = True
    $ achievement.grant("erika1")

    return


label erikaend2:
    show erika grin at right with easeinright
    e "Oh, look who finally decided to wake up."
    h "Huh?"
    e "What time do you think it is?"
    show haru yukata hmm
    h "...Time for breakfast?"
    e "Breakfast was over ages ago. It's almost time to check out."
    show haru yukata panicked
    h "What? I need to change!"
    show erika
    e "Calm down. Manami is dealing with that, so you still have some time."
    h "Oh..."
    show haru yukata down
    h "I caused trouble for Manami again..."
    show erika isee
    e "Hey."
    e "Do you have like, the world's lowest sense of self-worth or something?"
    show haru yukata panicked
    h "Huh?"
    e "You \"caused trouble for Manami again\"?"
    e "Are you kidding me?"
    e "She just went to go check out."
    e "What part of that is \"trouble\"?"
    e "She's your best friend, right?"
    e "Would you think of helping her out as \"trouble\"?"
    show haru yukata ganba
    h "Of course not!"
    show erika
    e "Exactly. It's the same for Manami."
    show haru yukata blush
    h "..."
    e "Wow, you're really helpless, aren't you?"
    e "Come on. Hurry up and get dressed - Manami's waiting in the lobby."

    scene bg reception
    show haru at left
    show manami at midright
    show erika at right
    with fade

    m "Hi! I just finished checking us out."
    h "Thanks, Manami."
    show manami hehe
    m "It's nothing!"
    m "Oh, and also - I just got a message from my boyfriend!"
    m "He says he wants to treat all of us to lunch!"
    m "He wants to meet you two!"
    show haru tsuyoki
    h "Oh... That's wonderful."

    show erika isee
    e "Manami, I'd love to..."

    show erika isee at midleft
    show manami at right
    with ease

    e "Actually, I was going to take Haru on a tour around the town after this."
    e "Sorry!"

    show manami surprised
    m "Really?"

    show haru panicked
    h "What?"

    e "You know, since Haru didn't get to go into the women's baths..."
    e "I just felt really bad for her, so I thought I'd take her out for a bit."

    show manami worried

    m "Then I'll go too!"

    e "No, no. Go meet your boyfriend."
    e "It's your birthday weekend. I'm sure he's got something planned for you."

    m "But..."
    m "Haru, will you be OK?"

    menu:
        h "What? Me?"
        "I'll be fine":

            pass
        "...":
            h "..."
            e "Haru?"
            h "(I don't know what Erika's thinking, but...)"
            menu:
                h "(...I don't really want to meet Manami's boyfriend right now.)"
                "I'll be fine":

                    pass

    show haru
    h "I'll be fine, Manami."
    h "Say hi to your boyfriend for us."

    show manami
    m "OK then."
    show manami hehe
    m "It makes me happy to see you two getting along!"
    m "Take good care of Haru for me, Erika!"
    m "I'll head out first then."

    h "See you."
    show erika grin
    e "See you later, Manami."

    hide manami with moveoutright
    h "..."
    h "So we're taking a tour around town?"

    show erika
    e "Nah, I just figured that you wouldn't want to meet up with Manami's boyfriend."
    e "But if I didn't say anything, you would've just agreed, right?"
    show haru hmm
    h "...Probably."
    show erika isee
    e "Hopeless."
    e "Anyway, I do actually want to take a look around town."
    e "Not sure where to go though."
    show haru
    show staff at right with easeinright

    s "Oh! Good morning. Miss Nagata, yes?"

    if rotenburo == 1:
        h "(The lady who upgraded our room...!)"

        h "Thank you very much for yesterday."
    else:
        e "This is the attendant who told me that the baths are empty at night!"
        h "Oh! Thank you very much."
    show staff bow
    s "It was nothing."

    show staff
    s "If you are planning to visit the town, may I suggest the hot spring in this flyer?"

    e "Oh?"

    s "They have lovely private baths that can be reserved by anyone."
    s "My older sister often goes there."

    h "Your older sister?"

    s "Yes. She also finds it hard to go into women's baths when there are many people about."

    show haru panicked
    h "Oh! Is your sister also..."

    show staff bow

    s "Yes. So I just wanted to say..."
    s "I hope you have a wonderful time here at the hot springs."
    s "Forgive my intrusion."

    hide staff with moveoutright

    h "..."
    show erika grin
    e "Wow, that was pretty cool."
    h "Yeah."
    e "Guess we should take the lady's advice!"
    e "Want to check out the reserved baths?"

    show haru blush
    h "Yeah, that'd be nice..."

    e "Let's go then!"

label erika2:
    $ _skipping = False
    $ quick_menu = False
    scene cg erikaend2
    with fade

    show text "{font=tl/None/npckc.ttf}ERIKA END 2)\nTHE WORLD CAN BE KIND TOO{/font}" at credits with Dissolve(1.5)
    pause
    hide text with dissolve
    show text "{font=tl/None/npckc.ttf}CREDITS\nStory/Code/Art: npckc\nMusic: maxdotine & npckc\nSE: Pocket Sound\n\nThank you for playing!{/font}" at credits with Dissolve(1.5)
    pause
    stop music fadeout 3.0
    scene black with Dissolve(3.0)
    $ _skipping = True
    $ persistent.erika2 = True
    $ achievement.grant("erika2")

    return

label manamiend1:
    show manami at right with easeinright
    m "Good morning, Haru!"
    h "Good morning, Manami."
    h "Nagata is still asleep."
    m "Yeah, I thought so!"
    m "I don't think she'll wake up before breakfast."
    h "Oh..."
    m "It's OK! We can just buy something on the way home."
    m "We still need to go souvenir shopping too!"
    show haru yukata hmm
    h "Souvenirs, huh..."
    h "I never know what to buy."
    h "There are always so many kinds..."
    show manami hehe
    m "Hehe."
    show haru yukata
    h "What is it?"
    m "You said that before too."
    h "Really?"
    m "Yup! On our school trip when we were still junior high students."
    m "We were buying souvenirs on the last day."
    m "Everyone was already finished, but you still hadn't decided."
    m "You said there were too many kinds for you to choose just one."
    m "So in the end, we ran out of time and you didn't buy anything!"
    show haru yukata hmm
    h "Ah, yeah, I remember that..."
    h "You ended up sharing yours with me."
    show manami
    m "Haha, I did!"
    m "You really haven't changed at all, Haru."
    m "Even though we've been friends so long."
    h "Haha..."
    m "Anyway, I'm going to go check us out first, so why don't you get changed?"
    m "After Erika wakes up, come down to the lobby!"
    show haru yukata
    h "OK. See you later."
    hide manami with moveoutright
    h "..."
    show haru yukata down
    h "I wonder if I really haven't changed..."

    scene bg reception
    show haru at left
    show erika at right
    show manami at midright
    with fade

    m "Hi! Are you ready to go?"

    e "Yeah, I'm ready."

    h "..."

    m "Haru?"

    h "Yeah, let's go."

    h "I'll need the time to choose my souvenir."

    show manami hehe
    m "Hehe."
    m "Don't worry! I'll help you pick this time."

    show erika grin
    e "What, does Suzuki need help choosing souvenirs?"

    e "They have some really good red-bean pancakes here, apparently."

    m "Really? I love red-bean pancakes!"

    h "Let's go take a look then."

    m "Yeah!"

label manami1:
    $ _skipping = False
    $ quick_menu = False
    scene cg manamiend1
    with fade

    show text "{font=tl/None/npckc.ttf}MANAMI END 1)\nFRIENDS FOREVER...{/font}" at credits with Dissolve(1.5)
    pause
    hide text with dissolve
    show text "{font=tl/None/npckc.ttf}CREDITS\nStory/Code/Art: npckc\nMusic: maxdotine & npckc\nSE: Pocket Sound\n\nThank you for playing!{/font}" at credits with Dissolve(1.5)
    pause
    stop music fadeout 3.0
    scene black with Dissolve(3.0)

    $ _skipping = True
    $ persistent.manami1 = True
    $ achievement.grant("manami1")

    return

label manamiend2:
    show manami yukata at right with easeinright

    m "Oh! Haru, you're awake."
    m "Good morning."
    h "What time is it?"
    m "A little late. We should check out soon."
    h "Oh..."
    show haru yukata down
    h "(I said I would give Manami the present...)"
    h "(So if I don't give it to her, she'll think it's weird...)"
    h "..."
    m "Haru?"
    h "Would you close your eyes for a moment?"
    m "OK?"
    scene black
    with fade
    h "OK, just stay still for a moment."
    m "Sure, but why?"
    h "Just wait."
    m "OK..."
    h "..."
    h "OK, you can open your eyes."
    scene bg room
    show haru yukata at left
    show manami yukata at right
    h "Happy birthday."
    h "I put my present for you in your bag..."
    h "But don't open it until you get home, OK?"
    show manami yukata worried
    m "Why?"
    show haru yukata down
    h "Please... just don't."
    m "OK..."
    m "...Haru, is there anything you want to tell me?"
    m "If you do, I want you to tell me. No matter what it is."
    h "..."
    h "Did you hear me talking yesterday?"
    m "..."
    m "I did..."
    m "But you never tell me anything, Haru."
    m "Even when I'm worried, if I ask, you just tell me you're fine."
    m "Even when you're obviously not fine!"
    m "But I don't want to pry..."
    m "If I had known you were having a tough time at school, I would've..."

    show haru yukata
    h "Sorry, Manami..."
    h "I just didn't want to trouble you..."
    m "Trouble me?"
    m "You're my best friend!"
    m "You could never be trouble to me!"
    m "You mean the world to me..."
    m "I'm so sorry I couldn't do anything to help."

    show haru yukata panicked
    h "No! It's not your fault! I never told you anything..."
    show haru yukata down
    h "I just... I just didn't want you to treat me differently."
    h "Everyone treats me differently because... because I'm trans."
    h "But not you, Manami."
    h "You've always treated me the same. As your friend."
    h "And I was so scared of doing anything that might change that..."
    m "Haru..."
    h "I'm sorry, Manami."
    m "No... I'm sorry you felt you couldn't tell me."
    m "Nothing you say could ever change how I feel about you."
    m "You will always be my oldest and dearest friend."
    show haru yukata
    h "Manami..."

    m "...I want you to be honest with me."
    m "Did I make you uncomfortable by asking you to come on this trip?"

    menu:
        h "..."
        "I'm happy you asked":
            h "I'm happy you asked me."
            h "I did feel a bit unsure about what to do, but..."
            h "I felt really happy you invited me to this girls-only trip..."
            show manami yukata
            m "Of course I invited you!"
        "A little uncomfortable":

            h "I did feel a bit uncomfortable, to be honest."
            h "I wasn't sure I really belonged on this girls-only trip..."
            show manami yukata
            m "Of course you do!"


    show haru yukata blush
    h "Thanks, Manami..."

    m "Promise me you won't keep any more secrets?"
    h "I promise."

    m "Is there anything else you want to tell me before we go?"

    show haru yukata down
    menu:
        h "..."
        "Not right now":
            h "I've told you everything I want to tell you right now."
        "I've told you everything":
            h "I've said everything I want to say."

    show haru yukata
    h "But... if you have any questions, I promise I'll answer them honestly too."

    show manami yukata hehe
    m "Thanks, Haru..."
    m "For talking to me, and for the present."

    show haru yukata blush
    h "No... Thank you for listening, and accepting the present."

    show manami yukata
    m "Haru..."

    show manami yukata at midright with ease
    show erika yukata at right with easeinright
    e "Morning."
    e "You two are up early."

    show manami yukata surprised
    m "It's not early at all! We have to go check out soon!"
    e "Shouldn't we be getting ready to go then?"
    m "We really should! We need to get changed!"

    scene bg reception
    show haru at left
    show manami at midright
    show erika at right
    with fade

    m "We managed to check out in time..."
    e "Somehow."
    m "I'm hungry though..."
    h "Well, we haven't eaten breakfast."
    e "Want to go see what there is to eat in town?"
    e "We haven't really had a chance to look around."
    show manami hehe
    m "Oh, that sounds fun!"
    h "I think I'll head back first."
    show manami surprised
    m "Did you have something to do today?"

    h "I'm just a bit tired, that's all."

    show erika isee
    e "That's too bad."

    e "Want to head out then, Manami?"

    show manami worried
    m "Will you be OK on your own, Haru?"

    h "I'll be fine."
    h "I promise."

    show manami
    m "OK then!"
    m "Let's go, Erika!"
    m "See you later, Haru!"

    show erika
    e "See you, Suzuki."

    h "Bye."

    hide manami
    hide erika
    with moveoutright

    h "..."
    h "This was for the best."
    h "I hope Manami likes her present."

label manami2:

    $ _skipping = False
    $ quick_menu = False
    scene cg manamiend2
    with fade

    show text "{font=tl/None/npckc.ttf}MANAMI END 2)\nHONESTY IS LIKE A GIFT{/font}" at credits with Dissolve(1.5)
    pause
    hide text with dissolve
    show text "{font=tl/None/npckc.ttf}CREDITS\nStory/Code/Art: npckc\nMusic: maxdotine & npckc\nSE: Pocket Sound\n\nThank you for playing!{/font}" at credits with Dissolve(1.5)
    pause
    stop music fadeout 3.0
    scene black with Dissolve(3.0)

    $ _skipping = True
    $ persistent.manami2 = True
    $ achievement.grant("manami2")

    return

label normalend:
    show manami at midright
    show erika at right
    e "Hey, sleepyhead."
    m "Erika, you were sleeping until five minutes ago."
    show erika grin
    e "That was five minutes ago. This is now."
    e "You should get changed! It's time to check out."
    m "Erika and I will go down to the lobby first."
    h "OK, I'll see you later."
    m "See you!"
    e "Don't take too long!"
    hide manami
    hide erika
    with moveoutright
    h "..."
    h "Time to change out of this yukata then."
    scene bg reception
    show manami at midright
    show erika at right
    show haru at left
    with fade
    h "Did you finish checking out?"
    show erika grin
    e "Ages ago."
    m "You can ignore Erika. We just finished."
    show erika isee
    e "That's so mean, Manami."
    m "Shush."
    m "We were talking about eating breakfast in town, but what do you think?"
    h "Breakfast?"

    h "That's a good idea."
    h "We haven't looked around town yet."

    show erika grin
    e "Awesome!"
    e "I'll go check the bus schedule."
    hide erika with moveoutright
    show manami at right with ease

    m "You seem to be in a good mood."
    show haru hmm
    h "Really?"
    show manami hehe
    m "Yup!"
    m "Did you enjoy the trip?"

    menu:
        h "(Did I enjoy the trip?)"
        "It was great":

            h "It was great."
            show manami
            m "Hehe, I'm glad to hear it!"
        "It was a bit tiring":
            h "It was a bit tiring."
            show manami worried
            m "Oh no! Are you OK?"
            h "I still enjoyed it though."
            show manami
            m "That's good then."

    show manami at midright with ease
    show erika at right with easeinright

    e "Hey! The bus is gonna be here soon!"

    show manami surprised
    show haru panicked
    m "OK, let's go!"
    show manami at midleft with ease
    m "Come on, Haru!"
    hide manami
    hide haru
    hide erika
    with moveoutright

label normal:

    $ _skipping = False
    $ quick_menu = False
    scene cg normalend
    with fade

    show text "{font=tl/None/npckc.ttf}GOOD END)\nHOT SPRINGS ARE OK{/font}" at credits with Dissolve(1.5)
    pause
    hide text with dissolve
    show text "{font=tl/None/npckc.ttf}CREDITS\nStory/Code/Art: npckc\nMusic: maxdotine & npckc\nSE: Pocket Sound\n\nThank you for playing!{/font}" at credits with Dissolve(1.5)
    pause
    stop music fadeout 3.0
    scene black with Dissolve(3.0)
    $ _skipping = True
    $ persistent.normal = True
    $ achievement.grant("normal")

    return

label badend:
    h "It doesn't look like anyone else is awake yet..."
    show haru yukata down
    h "..."
    h "I think I'll get changed."

    scene bg reception
    show haru down at left
    with fade

    h "..."
    h "I left a note in the room telling Manami I would be leaving first."
    h "...I'm just a bit too exhausted to talk to anyone right now."
    h "I tried my best to enjoy this hot spring trip, but..."
    h "...I guess it's just impossible for me."
    h "I just want to go home to my bed..."
    h "...I'll apologise to Manami over the phone later."
    h "For now... I just don't want to be here anymore."

label bad1:
    $ _skipping = False
    $ quick_menu = False
    scene cg badend1
    with fade

    show text "{font=tl/None/npckc.ttf}BAD END)\nHOT SPRINGS ARE NOT OK{/font}" at credits with Dissolve(1.5)
    pause
    hide text with dissolve
    show text "{font=tl/None/npckc.ttf}CREDITS\nStory/Code/Art: npckc\nMusic: maxdotine & npckc\nSE: Pocket Sound\n\nThank you for playing!{/font}" at credits with Dissolve(1.5)
    pause
    stop music fadeout 3.0
    scene black with Dissolve(3.0)

    $ _skipping = True
    $ persistent.bad1 = True
    $ achievement.grant("bad1")

    return

label purchase_support:
    scene black
    $ iap.purchase("support")
    if iap.has_purchased("support"):
        "Thank you for your support!"
    else:
        "Payment cancelled."
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
