"""
-----------------------------------------
@Author: xuhuanjun
@Email: 20212010075@fudan.edu.cn
@Created: 2021/11/1
------------------------------------------
@Modify: 2021/11/1
------------------------------------------
@Description:
"""
import string
import random

from kgdt.models.graph import GraphData
from tqdm import tqdm

from sckg.buildtrie import Buildtrim


class SoftwareKG:
    def __init__(self, graph_path, trie_path=None):
        self.graph: GraphData = GraphData.load(graph_path)
        self.trie: Buildtrim = Buildtrim.load(trie_path)

    def is_exist_concept(self, word):
        if not self.graph.find_nodes_by_property("concept_name", word):
            return False
        return True

    def get_node_num(self):
        return self.graph.get_node_num()

    def get_relation_num(self):
        return self.graph.get_relation_num()

    def get_node_ids(self):
        return self.graph.get_node_ids()

    def print_graph_info(self):
        return self.graph.print_graph_info()

    def get_node_info_by_id(self, nodeid):
        return self.graph.get_node_info_dict(nodeid)

    def get_concept_by_id(self, id):
        return self.get_node_info_by_id(id)['properties']['concept_name']

    def get_node_by_concept(self, word):
        return self.graph.find_nodes_by_property("concept_name", word)

    def get_id_by_concept(self, word):
        node = self.graph.find_nodes_by_property("concept_name", word)
        if node:
            return node[0]['id']
        return []

    def get_concept_score(self, word):
        node = self.graph.find_nodes_by_property("concept_name", word)
        return node[0]['properties']['score']

    def get_concept_labels(self, word):
        node = self.graph.find_nodes_by_property("concept_name", word)
        return node[0]['labels']

    def get_all_concept(self):
        concepts = []
        for node_id in self.graph.get_node_ids():
            node = self.graph.get_node_info_dict(node_id)
            concept_name = node['properties']['concept_name']
            concepts.append(concept_name)
        return concepts

    def is_exist_is_a_relation(self, start_word, end_word, relationtype='is a'):
        start_id = self.get_id_by_concept(start_word)
        end_id = self.get_id_by_concept(end_word)
        return self.graph.exist_relation(startId=start_id, relationType=relationtype, endId=end_id)

    def is_action(self, word):
        node = self.get_node_by_concept(word)
        labels = node[0]['labels']
        if 'action' in labels:
            return True
        return False

    def is_characteristic(self, word):
        node = self.get_node_by_concept(word)
        labels = node[0]['labels']
        if 'characteristic' in labels:
            return True
        return False

    def is_concept(self, word):
        node = self.get_node_by_concept(word)
        labels = node[0]['labels']
        if 'characteristic' in labels or 'action' in labels:
            return False
        return True

    def find_out_is_a_relation_concept(self, start_word):
        out_relations = self.get_out_relations(start_word)
        result = []
        for relation in out_relations:
            if relation[1] == 'is a':
                result.append(relation[2])
        return result

    def find_out_is_a_relation_concept_by_id(self, id):
        start_word = self.get_concept_by_id(id)
        # print(start_word)
        out_relations = self.get_out_relations(start_word)
        result = []
        for relation in out_relations:
            if relation[1] == 'is a':
                node = self.get_node_by_concept(relation[2])
                result.append(node)
        return result

    def find_in_is_a_relation_concept(self, start_word):
        in_relations = self.get_in_relations(start_word)
        result = []
        for relation in in_relations:
            if relation[1] == 'is a':
                result.append(relation[0])
        return result

    def find_out_facet_of_relation_concept(self, start_word):
        out_relations = self.get_out_relations(start_word)
        result = []
        for relation in out_relations:
            if relation[1] == 'facet of':
                result.append(relation[2])
        return result

    def find_out_facet_of_relation_concept_by_id(self, id):
        start_word = self.get_concept_by_id(id)
        out_relations = self.get_out_relations(start_word)
        result = []
        for relation in out_relations:
            if relation[1] == 'facet of':
                node = self.get_node_by_concept(relation[2])
                result.append(node)
        return result

    def find_in_facet_of_relation_concept(self, start_word):
        in_relations = self.get_in_relations(start_word)
        result = []
        for relation in in_relations:
            if relation[1] == 'facet of':
                result.append(relation[0])
        return result

    def process_relation(self, relation):
        node_a = self.get_concept_by_id(relation[0])
        node_b = self.get_concept_by_id(relation[2])
        tup = (node_a, relation[1], node_b)
        return tup

    def get_in_relations(self, concept):
        node_id = self.get_id_by_concept(concept)
        relations = self.graph.get_all_in_relations(node_id)
        results = []
        for relation in relations:
            tup = self.process_relation(relation)
            results.append(tup)
        return results

    def get_out_relations(self, concept):
        id = self.get_id_by_concept(concept)
        relations = self.graph.get_all_out_relations(id)
        results = []
        for relation in relations:
            tup = self.process_relation(relation)
            results.append(tup)
        return results

    def is_exit_facet_of_relation(self, start_word, end_word, relationtype='facet of'):
        start_id = self.get_id_by_concept(start_word)
        end_id = self.get_id_by_concept(end_word)
        return self.graph.exist_relation(startId=start_id, relationType=relationtype, endId=end_id)

    def is_exit_relation(self, start_word, end_word):
        start_id = self.get_id_by_concept(start_word)
        end_id = self.get_id_by_concept(end_word)
        return self.graph.exist_any_relation(start_id, end_id)

    def get_all_relations(self, start_word, end_word):
        start_id = self.get_id_by_concept(start_word)
        end_id = self.get_id_by_concept(end_word)
        return self.graph.get_all_relations(start_id, end_id)

    def find_all_shortest_paths(self, start_word, end_word):
        start_id = self.get_id_by_concept(start_word)
        end_id = self.get_id_by_concept(end_word)
        return self.graph.find_all_shortest_paths(start_id, end_id)

    def find_common_out_relationship_node(self, concept1, concept2):
        concept1_id = self.get_id_by_concept(concept1)
        concept2_id = self.get_id_by_concept(concept2)

        concept1_relations = self.graph.get_all_out_relations(concept1_id)
        concept2_relations = self.graph.get_all_out_relations(concept2_id)

        comment_relations = []
        for relation1 in concept1_relations:
            for relation2 in concept2_relations:
                if relation1[2] == relation2[2] and relation1[1] == relation2[1]:
                    comment_relations.append(self.get_concept_by_id(relation2[2]))
        return comment_relations

    def find_common_in_relationship_node(self, concept1, concept2):
        concept1_id = self.get_id_by_concept(concept1)
        concept2_id = self.get_id_by_concept(concept2)

        concept1_relations = self.graph.get_all_in_relations(concept1_id)
        concept2_relations = self.graph.get_all_in_relations(concept2_id)

        comment_relations = []
        for relation1 in concept1_relations:
            for relation2 in concept2_relations:
                if relation1[0] == relation2[0] and relation1[1] == relation2[1]:
                    comment_relations.append(self.get_concept_by_id(relation2[0]))
        return comment_relations

    def find_include_prefix_concept(self, concept):
        return self.trie.tree.items(prefix=concept)

    def find_all_concept_from_sentence(self, sentence):
        # 给一段文本，返回在KG里面出现的概念
        concepts = []
        sentence = sentence.lower()
        sentence = sentence.translate(str.maketrans('', '', string.punctuation))
        words = sentence.strip("\n").lower().split()
        for i, word in enumerate(words):
            concept = word
            if i == len(words) - 1:
                break
            for j in range(i + 1, i + 5):
                if j < len(words):
                    concept = concept + " " + words[j]
                if self.is_exist_concept(concept):
                    concepts.append(concept)
        for word in words:
            if not self.is_exist_concept(word) and not self.is_concept(word):
                continue
            concepts.append(word)
        concepts = set(concepts)
        return concepts

    def is_exit_concept_in_sentence(self, concept, sentence):
        concepts = self.find_all_concept_from_sentence(sentence)
        if concept in concepts:
            return True
        return False

    def find_longest_valid_concept_from_sentence(self, sentence):
        # 给一段文本，返回在KG里面出现的有效最长概念
        concepts = []
        sentence = sentence.lower()
        sentence = sentence.translate(str.maketrans('', '', string.punctuation))
        words = sentence.strip("\n").lower().split()
        index = 0
        while index < len(words):
            concept = words[index]
            longest_concept = concept
            for j in range(index + 1, index + 6):
                if j < len(words):
                    concept = concept + " " + words[j]
                    if self.is_exist_concept(concept):
                        longest_concept = concept
                        index = j
            if self.is_exist_concept(longest_concept) and self.is_concept(longest_concept):
                concepts.append(longest_concept)
            index = index + 1
        return concepts

    def find_longest_concept_from_sentence(self, sentence):
        # 给一段文本，返回在KG里面出现的最长概念
        concepts = []
        sentence = sentence.lower()
        sentence = sentence.translate(str.maketrans('', '', string.punctuation))
        words = sentence.strip("\n").lower().split()
        index = 0
        while index < len(words):
            concept = words[index]
            longest_concept = concept
            for j in range(index + 1, index + 6):
                if j < len(words):
                    concept = concept + " " + words[j]
                    if self.is_exist_concept(concept):
                        longest_concept = concept
                        index = j
            if self.is_exist_concept(longest_concept):
                if self.is_concept(longest_concept):
                    concepts.append((longest_concept, 'valid'))
                else:
                    concepts.append((longest_concept, 'invalid'))
            index = index + 1
        return concepts

    def get_upper_concept(self, concept):
        id = self.get_id_by_concept(concept)
        if not id:
            return None
        relations = self.graph.get_all_out_relations(id)
        upper_concepts = []
        for relation in relations:
            if relation[1] == 'is a':
                upper_concepts.append(self.get_concept_by_id(relation[2]))
        return upper_concepts

    def get_common_upper_concept(self, concept_a, concept_b):
        a_id = self.get_id_by_concept(concept_a)
        b_id = self.get_id_by_concept(concept_b)
        if not a_id or not b_id:
            return None
        a_relations = self.graph.get_all_out_relations(a_id)
        b_relations = self.graph.get_all_out_relations(b_id)
        common_concepts = []
        for relation1 in a_relations:
            for relation2 in b_relations:
                if relation1[2] == relation2[2] and relation1[1] == relation2[1] == 'is a':
                    common_concepts.append(self.get_concept_by_id(relation2[2]))
        return common_concepts

    def get_random_node(self):
        count = []
        while len(count) < 5:
            number = random.randint(0, 222227)
            node = self.graph.get_node_info_dict(number)
            if not node:
                continue
            if float(node['properties']['score']) < 0.96:
                continue
            if not self.find_out_is_a_relation_concept(self.get_concept_by_id(number)):
                continue
            count.append(node)
        return count

    def get_random_lastest_node(self):
        count = []
        max_num = self.graph.get_node_num()
        while len(count) < 5:
            number = random.randint(max_num - 2000, max_num)
            # print(number)
            node = self.graph.get_node_info_dict(number)
            if not node:
                continue
            if not self.find_out_is_a_relation_concept(self.get_concept_by_id(number)):
                continue
            count.append(node)
        return count

    def get_hot_concepts(self):
        result = []
        for id in tqdm(self.graph.get_node_ids()):
            node = self.graph.get_node_info_dict(id)
            if not node:
                continue
            if not 'frequency' in node['properties']:
                continue
            f = node['properties']['sum_frequency']
            frequency = {
                "concept": node['properties']['concept_name'],
                "frequency": f,
                "id": id,
                "label": node['labels'],
                "properties": node['properties']
            }
            result.append(frequency)
        result = sorted(result, key=lambda e: e['frequency'], reverse=True)
        return result[0:10]
