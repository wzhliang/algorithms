#!env python2
import sys
from graph import DirectGraphFactory, DirectedGraphError


class TWC:
    def __init__(self, in_file, out_file):
        self.graph = DirectGraphFactory.new_graph(in_file)
        self.in_file = in_file
        self.out_file = out_file
        self.a2c = self.graph.find_all_paths('A', 'C')
        self.b2b = self.graph.find_all_paths('B', 'B')
        self.c2c = self.graph.find_all_paths('C', 'C')

    def _get_distance(self, route):
        try:
            return self.graph.get_distance(route)
        except DirectedGraphError:
            return "NO SUCH ROUTE"

    def q1(self):
        return self._get_distance(['A', 'B', 'C'])

    def q2(self):
        return self._get_distance(['A', 'D'])

    def q3(self):
        return self._get_distance(['A', 'D', 'C'])

    def q4(self):
        return self._get_distance(['A', 'E', 'B', 'C', 'D'])

    def q5(self):
        return self._get_distance(['A', 'E', 'D'])

    def q6(self):
        threes = [x for x in self.c2c if len(x) <= 4]
        return str(len(threes))

    def q7(self):
        fours = [x for x in self.a2c if len(x) == 5]
        return str(len(fours))

    def q8(self):
        dists = [self.graph.get_distance(x) for x in self.a2c]
        return str(min(dists))

    def q9(self):
        dists = [self.graph.get_distance(x) for x in self.b2b]
        return str(min(dists))

    def q10(self):
        dists = [self.graph.get_distance(x) for x in self.c2c]
        dists = [x for x in dists if x < 30]
        return str(len(dists))

    def main(self):
        with open(self.out_file, 'wt') as output:
            for i in range(1, 11):
                msg = getattr(self, 'q%d' % i)()
                print >> output, "Output #%d: %s" % (i, msg)


if __name__ == '__main__':
    twc = TWC(sys.argv[1], sys.argv[2])
    twc.main()
