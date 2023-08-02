class User:
    def __init__(self, first_name, last_name, email, age, is_rewards_member, gold_card_points, amount):
        self.first_name=first_name
        self.last_name=last_name
        self.email=email
        self.age=age
        self.is_rewards_member = is_rewards_member
        self.gold_card_points =gold_card_points
        self.amount=amount
    
    
    def display_info(self):
        print(f"First Name: {self.first_name}")
        print(f"Last name: {self.last_name}")
        print(f"Email: {self.email}")
        print(f"Age: {self.age}")
        if(self.is_rewards_member == False):
            print("No")
        else:
            print("Yes")
        print(f"Gold Card Points: {self.gold_card_points}")
        
    
    def enroll(self):
        if(self.is_rewards_member==True):
            print("User is already a member")
        else:
            self.is_rewards_member=True
            self.gold_card_points=200
            print("Congrats on your 200 Gold Card Points!")

    def spend_points(self,amount):
        if(self.amount<= self.gold_card_points):
            self.gold_card_points = self.gold_card_points-amount
            print(f"Amount You Spent: {self.amount} points.")
            print(f"You now have {self.gold_card_points} remaining")
        else:
            print("You have not earned enough points yet!")



user_michael = User("Michael","Warren","123@123.com",24,False,0,100)
User.display_info(user_michael)
User.enroll(user_michael)
User.spend_points(user_michael,100)
User.display_info(user_michael)

