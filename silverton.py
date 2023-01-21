from utils import *
class Game:
    turn = 1
    idn = get_idn(turn)
    items = {
        'gold': {
            'label':'Gold', 'value': 4, 'range': gold_range, 'update': update_gold
        }, 
        'copper': {
            'label': 'Copper', 'value': 4, 'range': copper_range, 'update': update_copper
        }, 
        'silver': {
            'label': 'Silver', 'value': 5, 'range': silver_range, 'update': update_silver
        }, 
        'lumber_denver': {
            'label': 'Lumber in Denver', 'value': 3, 'range': lumber_range[1:8], 'limit': 10, 'update': update_lumber
        },
        'lumber_slc': {
            'label': 'Lumber in SLC', 'value': 2, 'range': lumber_range[3:], 'limit': 8, 'update': update_lumber
        },
        'lumber_pueblo': {
            'label': 'Lumber in Pueblo', 'value': 3, 'range': lumber_range[1:8], 'limit': 6, 'update': update_lumber
        },
        'lumber_santafe': {
            'label': 'Lumber in Santa Fe', 'value': 3, 'range': lumber_range[:7], 'limit': 6, 'update': update_lumber
        },
        'lumber_elpaso': {
            'label': 'Lumber in El Paso', 'value': 3, 'range': lumber_range[1:8], 'limit': 8, 'update': update_lumber
        },
        'coal_denver': {
            'label': 'Coal in Denver', 'value': 3, 'range': coal_range[2:], 'limit': 16, 'update': update_coal_1
        },
        'coal_slc': {
            'label': 'Coal in SLC', 'value': 4, 'range': coal_range[:8], 'limit': 10, 'update': update_coal_1
        },
        'coal_pueblo': {
            'label': 'Coal in Pueblo', 'value': 3, 'range': coal_range[:7], 'limit': 8, 'update': update_coal_2
        },
        'coal_santafe': {
            'label': 'Coal in Santa Fe', 'value': 3, 'range': coal_range[1:9], 'limit': 8, 'update': update_coal_2
        },
        'coal_elpaso': {
            'label': 'Coal in El Paso', 'value': 3, 'range': coal_range[2:], 'limit': 8, 'update': update_coal_2
        }
    }

    def update_prices(self):
        for key, item in self.items.items():
            label = item.get('label')
            value = item.get('value')
            range = item.get('range')
            limit = item.get('limit', 10000)
            update_fun = item.get('update')
            how_many = prompt_user(label, limit)
            new_value = value + update_fun(how_many, self.idn)
            if new_value >= len(range):
                new_value = len(range) - 1
            if new_value < 0:
                new_value = 0

            self.items[key]['value'] = new_value

        # now that prices are set, increment turn
        self.turn += 1
        self.print_prices()

    def print_prices(self):
        turn_label = 'Turn: '+str(self.turn)
        if self.turn % 4 == 0:
            turn_label += ' - WINTER!'
        print(turn_label)
        for item in self.items.values():
            name = item.get('label')
            value = item.get('value')
            range = item.get('range')
            actual_value=range[value]
            print(name+': '+str(actual_value))

        self.update_prices()

def main():
    game = Game()
    print(game.print_prices())

main()