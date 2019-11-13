import numpy as np


class HilberCurveGenerator:
    def __init__(self):
        self.space_alphabet = 'ABCD'
        self.recurrence_matrix = np.array([[0, 3, 2, 1],
                                           [0, 1, 2, 3],
                                           [0, 1, 2, 3],
                                           [2, 1, 0, 3]
                                           ]
                                          )
        self.quad_mappings = {'A': np.array([-1.0, -1.0]),
                              'B': np.array([-1.0, 1.0]),
                              'C': np.array([1.0, 1.0]),
                              'D': np.array([1.0, -1.0])
                              }
        self.dimension_multiplier = 0.5

    def __recurse(self, base_array=None):
        if not base_array:
            base_array = self.space_alphabet

        next_results = []
        # Initial Run?

        if type(base_array) == str:
            base_array = np.array(list(base_array))
            # use idx to lookup reorder opperation to perform of base_array
            for idx, quad in enumerate(base_array):
                reorder_array = self.recurrence_matrix[idx]
                reordered_base = base_array[reorder_array]
                next_result = quad + '|' + ''.join(reordered_base)
                next_results.append(next_result)
        else:
            for quad_data in base_array:
                quad_base, base_array = quad_data.split('|')
                reordered_bases = self.__recurse(base_array=base_array)
                _ = [next_results.append(quad_base + reordered_base)
                     for reordered_base in reordered_bases]
        return next_results

    def __expand_last_recursion(self, quad_values):
        expanded_quads = []
        for quad_data in quad_values:
            quad_base, base_array = quad_data.split('|')
            _ = [expanded_quads.append(quad_base + sub_quad)
                 for sub_quad in base_array]
        return expanded_quads

    def __get_plot_data(self, quad_labels):
        '''Iterate through supplied quad labels sequentially and provide
           x & y coords for plotting x,y in range ]-1.0, 1.0[
        '''
        x_coords, y_coords = [], []
        for quad_label in quad_labels:
            position = None
            for depth, state in enumerate(quad_label):
                if not depth:
                    position = self.dimension_multiplier \
                        * self.quad_mappings[state]
                    continue
                position += (self.dimension_multiplier ** (depth + 1))\
                    * self.quad_mappings[state]

            x_coords.append(position[0])
            y_coords.append(position[1])

        return x_coords, y_coords

    def generate_curve(self, plot_depth):
        recursed_data = None

        for _ in range(1, plot_depth):
            if not recursed_data:
                recursed_data = self.__recurse(base_array=self.space_alphabet)
            else:
                recursed_data = self.__recurse(base_array=recursed_data)

            quad_labels = self.__expand_last_recursion(recursed_data)
            x_coords, y_coords = \
                self.__get_plot_data(quad_labels=quad_labels)
        return quad_labels


if __name__ == '__main__':
    hc_gen = HilberCurveGenerator()
    print(hc_gen.generate_curve(plot_depth=4))
