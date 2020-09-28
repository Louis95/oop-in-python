class Property:
    def __init__(self, square_feet='', beds='',
        baths='', **kwargs):
        super().__init__(**kwargs)
        self.square_feet = square_feet
        self.num_bedrooms = beds
        self.num_baths = baths
    
    def display(self):
        print("PROPERTY DETAILS")
        print("=======================================")

        print("square footage: {}".format(self.square_feet))
        print("bedrooms: {}".format(self.num_bedrooms))
        print("bathrooms: {}".format(self.num_baths))
        print()

    # @staticmethod
    def prompt_init():
        return dict(square=input("Enter the square feet: "),
                beds =input("Enter the number of bedrooms: "),
                bath=input("Enter the number of baths: "))
    
    prompt_init = staticmethod(prompt_init)


class Apartment(Property):
    valid_laundries = ("coin", "ensuite", "none")
    valid_balconies = ("yes", "No", "Solarium")

    '''
    **kwargs parameter is added to __init__ because we know it's going to be used in a multiple inheritance situation.
    '''  
    def __init__(self, balcony='', laundry='', **kwargs):
            super().__init__( **kwargs)
            self.balcony = balcony
            self.laundry = laundry
    
    def display(self):
        super().display()
        print("Apartment Details")
        print("laundry: %s" % self.laundry)
        print("has balcony: %s" % self.balcony)

    # @staticmethod
    def prompt_init():
            parent_init = Property.prompt_init()
            laundry = get_valid_input("What laundry facilities does "
                                    "the property have?",
                                    Apartment.valid_laundries)
            balcony = get_valid_input("Does the property have a balcony? ",
                                    Apartment.valid_balconies)

            parent_init.update({
                "laundry": laundry,
                "balcony": balcony
            })
            return parent_init
    prompt_init = staticmethod(prompt_init)

    

class House(Property):
    valid_garage = ("attached", "detached", "None")
    valid_fenced = ("yes", "no")

    def __init__(self, num_stories = ' ', garage= ' ', fenced= ' ',   **kwargs):
        super().__init__( **kwargs)
        self.garage = garage
        self.num_stories = num_stories
        self.fenced = fenced

    def display(self):
        super().display()
        print("HOUSE DETAILS")
        print("# of stories: {}".format(self.num_stories))
        print("garage: {}".format(self.garage))
        print("fenced yard: {}".format(self.fenced))
    
    # @staticmethod
    def prompt_init():
        parent_init = Property.prompt_init()
        fanced = get_valid_input("Is the yard fanced? ", House.valid_fenced)
        garage = get_valid_input("Is there a garage? ", House.valid_garage)
        num_stories = input("How many stories? ")

        parent_init.update({
            "fanced": fanced,
            "garage": garage,
            "num_stories": num_stories
        })

        return parent_init
    prompt_init = staticmethod(prompt_init)

class Purchase:
    def __init__(self, price='', taxes='', **kwargs):
        super().__init__(**kwargs)
        self.price = price
        self.taxes = taxes
    
    def display(self):
        super().display()
        print("PURCHASE DETAILS")
        print("selling price: {}".format(self.price))
        print("estimated taxes: {}".format(self.taxes))
    
    # @staticmethod
    def prompt_init():
        return dict(
            price = input("What is the selling price? "),
            taxes=input("What are the estimated taxes? ")
        )
    prompt_init = staticmethod(prompt_init)

class Rental:
    def __init__(self, furnished='', utilities='', rent='', **kwargs):
        super().__init__(**kwargs)
        self.furnished = furnished 
        self.rent = rent 
        self.utilities = utilities
    
    def display(self):
        super().display()
        print("RENTAL DETAILS")
        print("rent: {}".format(self.rent))
        print("estimated utilities: {}".format(self.utilities))
        print("furnished: {}".format(self.furnished))
    
    # @staticmethod
    def prompt_init():
        return dict(
            rent=input("What is the monthly rent? "),
            utilities=input("What are the estimated utilities? "),
            furnished = get_valid_input("Is the property furnished? ", ("yes", "no")))
    prompt_init = staticmethod(prompt_init)

'''
These two classes don't have a superclass (other than object), 
but we still call super().__init__ because they are going to be combined with the other classes,
and we don't know what order the super calls will be made in. The interface is similar
to that used for House and Apartment, which is very useful when we combine the functionality of these four classes in separate subclasses.
'''
class HouseRental(Rental, House):

    @staticmethod
    def prompt_init():
        init = House.prompt_init()
        init.update(Rental.prompt_init())
        return init
    # prompt_init = staticmethod(prompt_init)

class ApartmentRental(Rental, Apartment):

    @staticmethod
    def prompt_init():
        init = Apartment.prompt_init()
        init.update(Rental.prompt_init())
        return init

class ApartmentPurchase(Purchase, Apartment):

    @staticmethod
    def prompt_init():
        init = Apartment.prompt_init()
        init.update(Purchase.prompt_init())
        return init

class HousePurchase(Purchase, House):
    @staticmethod
    def prompt_init():
        init = House.prompt_init()
        init.update(Purchase.prompt_init())
        return init

class Agent:
    def __init__(self):
        self.property_list = []
    
    def display_properties(self):
        for property in self.property_list:
            property.display()
    
    type_map = {
        ("house", "rental"): HouseRental,
        ("house", "purchase"): HousePurchase,
        ("apartment", "rental"): ApartmentRental,
        ("apartment", "purchase"): ApartmentPurchase
    }

    def add_property(self):
        property_type = get_valid_input(
            "What type of property? ",
            ("house", "apartment")).lower()
        
        payment_type = get_valid_input(
            "What payment type? ",
            ("purchase", "rental")).lower()
        
        PropertyClass = self.type_map[
            (property_type, payment_type)]
        init_args = PropertyClass.prompt_init()
        self.property_list.append(PropertyClass(**init_args))
        

def get_valid_input(input_string, valid_options):
        input_string += " ({}) ".format(", ".join(valid_options))
        response = input(input_string)
        while response.lower() not in valid_options:
            response = input(input_string)
        return response


