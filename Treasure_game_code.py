name = input("Please enter your name to continue\n").capitalize()
print(
    f"Hello {name}! and Welcome to Treasure Island Game.\n\
    Your Mission is to find the hidden Treasure."
)
print(
    "you were following the map for treasure and walking on the road suddenly, you see two different paths."
)
direction = input(
    "Enter the direction which you will like to move towards\
1) Right? or \
2) Left\n"
)
if direction == "1":
    print(
        """ 
                                ___......__             _
                        _.-'           ~-_       _.=a~~-_
--=====-.-.-_----------~   .--.       _   -.__.-~ ( ___===>
              '''--...__  (    \ \\\ { )       _.-~
                        =_ ~_  \\-~~~//~~~~-=-~
                         |-=-~_ \\   \\
                         |_/   =. )   ~}
                         |}      ||
                        //       ||
                      _//        {{
                   '='~'          \\_    =
                                   ~~'
        you were killed by dinosaur\n
                Game Over!"""
    )
else:
    print("You have reached sea")
    print(
        """
    ___ __ 
   (_  ( . ) )__                  '.    \   :   /    .'
     '(___(_____)      __           '.   \  :  /   .'
                     /. _\            '.  \ : /  .'
                .--.|/_/__      -----____   _  _____-----
_______________''.--o/___  \_______________(_)___________
       ~        /.'o|_o  '.|  ~                   ~   ~
  ~            |/    |_|  ~'         ~
               '  ~  |_|        ~       ~     ~     ~
      ~    ~          |_|O  ~                       ~
             ~     ___|_||_____     ~       ~    ~
   ~    ~      .'':. .|_|A:. ..::''.
             /:.  .:::|_|.\ .:.  :.:\   ~
  ~         :..:. .:. .::..:  .:  ..:.       ~   ~    ~
             \.: .:  :. .: ..:: ./
    ~      ~      ~    ~    ~         ~
               ~           ~    ~   ~             ~
        ~         ~            ~   ~                 ~"""
    )
    swim = input(
        "Do you like to swim or would like a boat?\n Kindly enter boat or swim\n"
    ).lower()
    if swim == "swim":
        print(
            """ 
                    .-._   _ _ _ _ _ _ _ _
         .-''-.__.-'00  '-' ' ' ' ' ' ' ' '-.
         '.___ '    .   .--_'-' '-' '-' _'-' '._
          V: V 'vv-'   '_   '.       .'  _..' '.'.
            '=.____.=_.--'   :_.__.__:_   '.   : :
                    (((____.-'        '-.  /   : :
                                      (((-'\ .' /
                                    _____..'  .'
                                   '-._____.-'
            The Sea is full of Crocodiles\n
                   Game Over!"""
        )
    else:
        print(
            """ 
                __/___            
          _____/______|           
  _______/_____\_______\_____     
  \              < < <       |    
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"""
        )

        print(
            "congratulations! you have reached the land and found the Mysterious doors"
        )
        print(
            """
            __________
           |  __  __  |  
           | |  ||  | |
           | |  ||  | |
           | |__||__| |
           |  __  __()|
           | |  ||  | |
           | |  ||  | |
           | |  ||  | |
           | |  ||  | |
           | |__||__| |
           |__________|"""
        )

        last_choice = input(
            "Please choose the door\n\
             1) Yellow Door\
             2) Green Door\
             3) Red Door"
        )

        if last_choice == "1":
            print(last_choice)
