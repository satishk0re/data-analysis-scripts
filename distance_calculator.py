import math


class DistanceCalculatorTest:
    def distance_calculator(p1, p2):

        '''Variable assignment is inappropriate,
         every individual variable should be assign separately.'''
        a,b,c,d = 5,3,2,4
        '''result = 0 is not necessary as we can get a distance
         value by passing the parameters value in single go and we do not need to
           append the result.'''
        result = 0
        '''There should be '*' sign in second term of equation between term 6 and (d-b'''
        distance = math.sqrt(a-b)*(a-c) + 6*(d-b)*(d-b)
        '''print would just print '0' '''
        print(result)


    def distance_improved(self, p1, p2):
        x1, y1 = p1
        x2, y2 = p2
        dist = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
        return dist

    def calculate_distances(self, param_1, param_2):

        if {type(param_1), type(param_2)}.difference([list, tuple]):
            raise TypeError("The input should be a list or a tuple.")

        elif type(param_1) == tuple and type(param_2) == tuple:
            return self.distance_improved(param_1, param_2)


        else:
            distances = []
            for cordi_1, cordi_2 in zip(param_1, param_2):
                distances.append(self.distance_improved(cordi_1, cordi_2))
            return distances



if __name__ == '__main__':
    dist_1 = DistanceCalculatorTest()
    p1 = (0,3)
    p2 = (4,0)
    
    # test the new method 'distance_improved' with two tuples
    print(dist_1.distance_improved(p1,p2))

    # test the new method 'calculate_distances' with two tuples
    print(dist_1.calculate_distances((7,34),(9,76)))

    # test the new method 'calculate_distances' with two lists
    print(dist_1.calculate_distances([(11.2,6.7),(6.8,7.2)],[(7.5,8.6),(7.9,4.4)]))

    # test the new method 'calculate_distances' with two dictionaries
    print(dist_1.calculate_distances({3:8,8:6},{12:7,7:9}))

