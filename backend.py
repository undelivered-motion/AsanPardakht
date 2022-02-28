class Database():
    def __init__(self):
        self.users = [] # list of User objects
        self.size = 0

    def add(self,user):
        self.users.append(user)
        self.size +=1
        return True

    def has_card_number(self,card_number):
        for u in self.users:
            if card_number in u.card_numbers:
                return True

    def has_sim_number(self,sim_number):
         for u in self.users:
            if sim_number in u.sim_numbers:
                return True

    def has_user(self, name):
        for u in self.users:
            if u.name==name:
                return True
        return False

    def get_user(self, name):
        for u in self.users:
            if u.name == name:
                return u
        return None

    def get_user_by_card(self, card_number):
        for u in self.users:
            if card_number in u.card_numbers:
                return u
        return None

    def get_user_by_sim(self, sim_number):
        for u in self.users:
            if sim_number in u.sim_numbers:
                return u
        return None


class User():
    def __init__(self,name, card_number, password, sim_number):
        self.name = name
        self.password = password
        self.card_numbers = []
        self.card_amounts = {}
        self.card_passwords= {}
        self.sim_numbers = {}
        self.card_numbers.append(card_number)
        self.card_passwords[card_number] = password
        self.card_amounts[card_number] = 100000
        self.sim_numbers[sim_number] = 0

    def add_card(self, card_number,password):
        if not card_number in self.card_numbers: # if the number is already in db, nothing changes
            self.card_numbers.append(card_number)
            self.card_amounts[card_number] = 100000
            self.card_passwords[card_number] = password

    def add_sim(self, sim_number):
        if not sim_number in self.sim_numbers: # if the number is already in db, nothing changes
            self.sim_numbers[sim_number] = 0

    def check_pass(self, card_number, password):
        if not card_number in self.card_numbers:
            return False
        return self.card_passwords[card_number]== password

    def has_amount(self, card_number, amount):
        if not card_number in self.card_numbers:
            return False
        return self.card_amounts[card_number]>= amount

    def withdraw(self, card_number, amount): # u should call has amount first, but just in case:
        if not self.has_amount(card_number, amount):
            return False
        self.card_amounts[card_number] -= amount
        return True

    def deposit(self, card_number, amount):
        if not card_number in self.card_numbers:
            return False
        self.card_amounts[card_number] += amount
        return True

    def get_balance(self, card_number):
        if not card_number in self.card_numbers:
            return None
        return self.card_amounts[card_number]

    def charge_sim(self, sim_number, amount ):
        if not sim_number in self.sim_numbers:
            return False
        self.sim_numbers[sim_number] += amount
        return True

my_database = Database()


'''
if user wants to add a new card number to existing entry,
it should leave sim empty and vice versa
'''
def make_acc(name,card_number,password, sim_number): #change
    global my_database

    if len(name)==0:
        return False
    if len(sim_number)==0 and len(card_number)==0:
        return False
    if len(card_number)!=0 and len(password)==0:
        return False

    if my_database.has_card_number(card_number) or my_database.has_sim_number(sim_number):
        return False #duplicate card/sim

    if my_database.has_user(name):
        user = my_database.get_user(name)
        if len(card_number):
            user.add_card(card_number,password)
        if len(sim_number):
            user.add_sim(sim_number)
        return True

    new_user = User(name,card_number,password, sim_number)
    my_database.add(new_user)
    return True


'''
returns:
    -1: Unknown error
    0 : success
    1 : mojudi nakafi
    2 : wrong info
'''
def charge_sim(sim_number, amount, card_number, card_pass):
    global my_database
    try:
        amount = int(amount)
    except:
        return 2
    # check if card info is valid
    if my_database.has_card_number(card_number):

        user = my_database.get_user_by_card(card_number)

        if user.check_pass(card_number, card_pass):

            if not user.has_amount(card_number, amount):
                return 1 # poor

            if my_database.has_sim_number(sim_number):
                sim_user = my_database.get_user_by_sim(sim_number)
            else:
                user.add_sim(sim_number)
                sim_user = user

            if not user.withdraw(card_number, amount):
                return -1
            if not sim_user.charge_sim(sim_number, amount):
                return -1
            return 0

        else:
            return 2 # wrong password
    else:
        return 2 # wrong card number



'''
return :
        0 success
        1 poor
        2 wrong source or source==dest
        3 wrong dest
        4 wrong pass
'''
def transaction(source_card, source_password, dest_card, amount):
    global my_database
    try:
        amount = int(amount)
    except:
        return 2

    if source_card==dest_card:
        return 2

    if not my_database.has_card_number(source_card):
        return 2

    if not my_database.has_card_number(dest_card):
        return 3

    source_user = my_database.get_user_by_card(source_card)
    if not source_user.check_pass(source_card, source_password):
        return 4

    dest_user = my_database.get_user_by_card(dest_card)


    if not source_user.has_amount(source_card, amount):
        return 1

    source_user.withdraw(source_card, amount)
    dest_user.deposit(dest_card, amount)

    return 0

def get_name_of_card_owner(card_number):
    global my_database
    if my_database.has_card_number(card_number):
        return my_database.get_user_by_card(card_number).name
    else:
        return ""

def get_balance(card_number, card_password):
    global my_database
    if my_database.has_card_number(card_number):
        user = my_database.get_user_by_card(card_number)
        if user.check_pass(card_number, card_password):
            return user.get_balance(card_number)
    return None



