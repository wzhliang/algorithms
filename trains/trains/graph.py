#!env python2


class DirectedGraphError(Exception):
    pass


class DirectedGraph(dict):
    def add_edge(self, edge):
        frm, to, weight = list(edge)
        if frm not in self.keys():
            self[frm] = {}
        self[frm].update({to: int(weight)})

    def find_edge(self, frm, to):
        try:
            return self[frm][to]
        except KeyError:
            raise DirectedGraphError

    def get_distance(self, path):
        edges = [self.find_edge(path[i], path[i + 1])
            for i in range(len(path) - 1)]
        return sum(edges)

    def been_there(self, path, frm, to):
        _path = ''.join(path)
        edge = "%s%s" % (frm, to)
        return edge in _path

    def find_all_paths(self, start, end, path=[]):
        path = path + [start]
        if start not in self:
            return []
        paths = []
        if start == end and len(path) > 1:  # no single stop path
            paths.append(path)
        for node in self[start]:
            if not self.been_there(path, start, node):
                newpaths = self.find_all_paths(node, end, path)
                for newpath in newpaths:
                    paths.append(newpath)
        return paths


class DirectGraphFactory(object):
    @staticmethod
    def new_graph(file):
        g = DirectedGraph()
        with open(file) as f:
            edges = f.readline().strip().split(':')[1].split(',')
            for e in edges:
                g.add_edge(e.strip())
        return g
