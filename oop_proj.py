class chatbook:

    __user_id = 1

    def __init__(self):
        self.id = chatbook.__user_id
        chatbook.__user_id +=1
        self.__name = 'default user'
        self.usr_name= ''
        self.pwd = ''
        self.loggedin = False
    
    @staticmethod
    def get_id(self):
        return chatbook.__user_id
    
    @staticmethod
    def get_id(self,val):
        chatbook.__user_id = val

    def get_name(self):
        return self.__name
    
    def set_name(self, value):
        self.__name = value

    def menu(self):
        usr_input= input("""Welcome to chatbook ! how would you like to proceed
                         1.press 1 to signup.
                         2.press 2 to signin.
                         3.press 3 to write a post.
                         4.press 4 to send a msg to frd.
                         5.press any key to exit
                         
                         ->""")
        if usr_input== 1:
            self.signup()
        elif usr_input==2:
            self.signin()
        elif usr_input==3:
            self.mypost()        
        elif usr_input==4:
            self.send_msg()
        else:
            exit()

    def signup(self):
        email = input("enter your email address -> ")
        pwd = input("setup your pass here -> ")
        self.usr_name = email
        self.pwd = pwd
        print("you have signed up sucessfully !")
        print("\n")
        self.menu()

    def signin(self):
        if self.usr_name=='' and self.pwd=='':
            print("you have to first sign up")
        else:
            usr = input("enter your user name or email here ->")
            pwd = input("enter your password here ->")
            if self.usr_name==usr and self.pwd==pwd:
                print("you have signin sucessfully !")
                self.loggedin = True
            else:
                print("please correct your credencial ")
        print("\n")
        self.menu()
        
    def mypost(self):
        if self.loggedin==True:
            txt = input("enter your message here -> ")
            print(f"the following message has been posted : {txt}")
        else:
            print("you have to signin first to write something...")
        print("\n")
        self.menu()

    def send_msg(self):
        if self.loggedin==True:
            txt = input("enter your message here -> ")
            frd = input("whom to send the message -> ")
            print(f"the following message has been sended to the {frd}")
        else:
            print("you have to signin first to write something...")
        print("\n")
        self.menu()
