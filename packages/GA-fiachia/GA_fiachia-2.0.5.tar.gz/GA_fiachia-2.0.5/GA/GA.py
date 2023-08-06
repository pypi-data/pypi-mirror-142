import random
import math

try:
    from printf import printf, color
    printf = printf.Format(_type=color.TYPE.ERROR).print
except:
    printf = print


class SameClass:
    def __init__(self, className: type, **kwargs):
        self.className = className
        self.kwargs = kwargs

    def set(self, *args):
        return self.className(*args, **self.kwargs)


class Gene:
    def __init__(self, value=None, length=0, maxValue=0, value_create_method=None, key_create_method=None):
        """

        :param value: [any]该基因对应的值，只有int类型不需要输入value_create_method
        :param length: [int]该基因的长度
        :param maxValue: [int]该基因的最大值
        :param value_create_method: [function]基因转换函数，将value值转换成int类型的值
        :param key_create_method: [function]权值生成函数，将value值转换成对应的权值
        """
        self.value_create_method = value_create_method
        self.key_create_method = key_create_method
        self.length = (length, maxValue)
        self.value = value

    @property
    def value(self):
        return self.__value

    @property
    def gene(self):
        return self.__gene

    @value.setter
    def value(self, value):
        self.__value = self.method(value)
        if self.__value > self.maxValue:
            self.__value = None
            self.__gene = bin(0)[2:].zfill(self.length)
        else:
            self.__gene = bin(self.__value)[2:].zfill(self.length)

    def set(self, value):
        self.value = value

    @property
    def length(self):
        return self.__length

    @property
    def maxValue(self):
        return self.__maxValue

    @length.setter
    def length(self, value):
        if isinstance(value, int):
            if value == 0:
                self.__length = 8
                self.__maxValue = 256
            else:
                self.__length = value
                self.__maxValue = pow(2, value)
        elif isinstance(value, (tuple, list)):
            if value[0] == 0 and value[1] == 0:
                self.__length = 8
                self.__maxValue = 256
            elif value[0] != 0 and value[1] != 0:
                self.__length = value[0]
                self.__maxValue = min(value[1], pow(2, value[0]))
            elif value[0] != 0:
                self.__length = value[0]
                self.__maxValue = pow(2, value[0])
            else:
                self.__length = math.ceil(math.log2(value[1]))
                self.__maxValue = value[1]
        else:
            self.__length = 8
            self.__maxValue = 256

    def method(self, value):
        if self.value_create_method is not None:
            try:
                return self.value_create_method(value)
            except:
                pass
        if value is None:
            return 0
        elif isinstance(value, int):
            return value
        else:
            return int(value)

    def __str__(self):
        return str(self.value)

    def __repr__(self):
        return str(self.value)

    def estimate(self, key_create_method=None):
        """
        评估函数

        :param key_create_method: [function]如果不输入则使用创建时输入的key_create_method，都没有则直接输出value值
        :return:
        """
        if key_create_method is not None:
            return key_create_method(self.value)
        elif self.key_create_method is not None:
            return self.key_create_method(self.value)
        else:
            return self.value

    def crossover_mutation(self, gene1, gene2=None, mutation_pro=0.5):
        """
        基因交换

        :param gene1: [any]第一个交换的基因，gene可以为值，根据self格式创建
        :param gene2: [any]第二个交换的基因，如果使用此参数，则不使用self本身进行交换
        :param mutation_pro: [float]交换概率
        :return: [list[Gene, ...]]
        """
        if not isinstance(gene1, Gene):
            gene1 = Gene(gene1, self.length, self.maxValue, self.value_create_method, self.key_create_method)
        if gene2 is None:
            gene2 = self
        elif not isinstance(gene2, Gene):
            gene2 = Gene(gene2, self.length, self.maxValue, self.value_create_method, self.key_create_method)
        if gene1.length != gene2.length:
            printf("您无法交换基因，父母物种隔离！")
            return list()
        gene_c1 = gene_c2 = ""
        for j in range(gene1.length):
            if random.random() >= mutation_pro:
                gene_c1 += gene1.gene[j]
                gene_c2 += gene2.gene[j]
            else:
                gene_c1 += gene2.gene[j]
                gene_c2 += gene1.gene[j]
        return [
            Gene(gene_c1, gene1.length, gene1.maxValue, bin_to_ten, gene1.key_create_method),
            Gene(gene_c2, gene1.length, gene1.maxValue, bin_to_ten, gene1.key_create_method),
        ]

    def mutation(self, gene=None, times=1, mutation_pro=0.1):
        """
        基因变异

        :param gene: [any]第一个变异的基因，gene可以为值，根据self格式创建，不输入则默认变异self
        :param times: [int]变异次数
        :param mutation_pro: [float]变异概率
        :return: [Gene or list[Gene, ...]]
        """
        if gene is None:
            gene = self
        elif not isinstance(gene, Gene):
            gene = Gene(gene, self.length, self.maxValue, self.value_create_method, self.key_create_method)
        if times == 1:
            gene_c = ""
            for j in range(gene.length):
                if random.random() >= mutation_pro:
                    gene_c += gene.gene[j]
                else:
                    gene_c += "0" if gene.gene[j] == "1" else "1"
            return Gene(gene_c, self.length, self.maxValue, bin_to_ten, self.key_create_method)
        gene_c_list = []
        for i in range(times):
            gene_c = ""
            for j in range(gene.length):
                if random.random() >= mutation_pro:
                    gene_c += gene.gene[j]
                else:
                    gene_c += "0" if gene.gene[j] == "1" else "1"
            gene_c_list.append(Gene(gene_c, self.length, self.maxValue, bin_to_ten, self.key_create_method))
        return gene_c_list

    def create_gene(self, gene):
        return Gene(gene, self.length, self.maxValue, self.value_create_method, self.key_create_method)


def bin_to_ten(bin_str):
    return int("0b%s" % bin_str)


class Chromosome:
    def __init__(self, *args: Gene, key_create_method=None, gene_template=None):
        self.gene_template = gene_template
        self.gene_list = args
        self.key_create_method = key_create_method

    @property
    def gene_template(self):
        return self.__gene_template

    @gene_template.setter
    def gene_template(self, value):
        if isinstance(value, Gene):
            self.__gene_template = value
        else:
            self.__gene_template = Gene()

    @property
    def gene_list(self):
        return self.__gene_list

    @gene_list.setter
    def gene_list(self, value):
        if isinstance(value, (tuple, list)):
            self.__gene_list = list()
            self.__length = 0
            for gene_i in value:
                if isinstance(gene_i, Gene):
                    self.__gene_list.append(gene_i)
                else:
                    self.__gene_list.append(self.gene_template.create_gene(gene_i))
                self.__length += 1
        else:
            printf("请输入合适的基因序列来构成染色体！")
            self.__gene_list = list()

    @property
    def length(self):
        return self.__length

    @length.setter
    def length(self, value):
        self.__length = len(self.__gene_list)

    def __str__(self):
        return "-".join([
            str(gene) for gene in self.gene_list
        ])

    def __repr__(self):
        return self.__str__()

    def add_static_gene(self, *genes):
        return Chromosome(
            *genes, *self.gene_list,
            key_create_method=self.key_create_method,
            gene_template=self.gene_template
        )

    def addGene(self, *genes):
        if genes:
            for gene in genes:
                if isinstance(gene, Gene):
                    self.gene_list.append(gene)
                    self.length = True
                else:
                    self.gene_list.append(self.gene_template.create_gene(gene))
                    self.length = True

    def setGene(self, gene, index=-1):
        if gene is not None:
            if isinstance(gene, Gene):
                self.gene_list.insert(index, gene)
            else:
                self.gene_list.insert(index, self.gene_template.create_gene(gene))

    def getGene(self, index=-1, is_mutation=False, mutation_pro=0.1):
        if is_mutation:
            return self.gene_list[index].mutation(mutation_pro=mutation_pro)
        return self.gene_list[index]

    def set_gene_list(self, *args):
        self.gene_list = args

    # 交叉遗传
    def crisscross_inheritance(self, father, mother=None, child_times=1, is_mutation=False, mutation_pro=0.1):
        if not isinstance(father, Chromosome):
            if isinstance(father, (tuple, list)):
                father = self.create_chromosome(*father)
            else:
                father = self.create_chromosome(father)
        if mother is None:
            mother = self
        elif not isinstance(mother, Chromosome):
            if isinstance(mother, (tuple, list)):
                mother = self.create_chromosome(*mother)
            else:
                mother = self.create_chromosome(mother)
        if father.length != mother.length:
            print("您无法生出孩子，父母物种隔离！")
            return list()
        children = list()
        for i in range(child_times):
            child_1 = list()
            child_2 = list()
            for j in range(0, father.length):
                if random.random() >= 0.5:
                    child_1.append(father.getGene(j, is_mutation, mutation_pro))
                    child_2.append(mother.getGene(j, is_mutation, mutation_pro))
                else:
                    child_1.append(mother.getGene(j, is_mutation, mutation_pro))
                    child_2.append(father.getGene(j, is_mutation, mutation_pro))
            children.append(self.create_chromosome(*child_1))
            children.append(self.create_chromosome(*child_2))
        return children

    def estimate(self, *args, key_create_method=None):
        """
        评估函数

        :param key_create_method: [function]如果不输入则使用创建时输入的key_create_method，都没有则为所有基因的评估和
        :return:[float]
        """
        if key_create_method is not None:
            return key_create_method(*args, *self.gene_list)
        elif self.key_create_method is not None:
            return self.key_create_method(*args, *self.gene_list)
        else:
            estimate_sum = 0
            for gene_i in self.gene_list:
                estimate_sum += gene_i.estimate()
            return estimate_sum

    def create_chromosome(self, *args):
        return Chromosome(*args, key_create_method=self.key_create_method, gene_template=self.gene_template)


def randint_choose(estimate_list, index):
    for i in range(len(estimate_list)):
        if index <= estimate_list[i]:
            return i
        index -= estimate_list[i]


class GA:
    def __init__(self, *args, maxItem=1, min_threshold=0, max_threshold=100, elimination_rate=0.5,
                 group_times=1, mutation_pro=0.3, static_value=None):
        self.chromosome_best_result_list = list()
        self.chromosome_list = self.chromosome_result = args
        self.maxItem = maxItem
        self.min_threshold = min_threshold
        self.max_threshold = max_threshold
        self.elimination_rate = elimination_rate
        self.group_times = group_times
        self.mutation_pro = mutation_pro
        self.static_value = static_value

    @property
    def chromosome_list(self):
        return self.__chromosome_list

    @chromosome_list.setter
    def chromosome_list(self, value):
        if isinstance(value, (tuple, list)):
            self.__chromosome_list = list()
            for value_i in value:
                if isinstance(value_i, Chromosome):
                    self.__chromosome_list.append(value_i)
                else:
                    printf("未输入染色体类，无法识别并使用")
        else:
            printf("未输入物种初始列表，无法识别并使用")

    @property
    def chromosome_result(self):
        return self.__chromosome_result

    @chromosome_result.setter
    def chromosome_result(self, value):
        if isinstance(value, (tuple, list)):
            self.__chromosome_result = list()
            for value_i in value:
                if isinstance(value_i, Chromosome):
                    self.__chromosome_result.append(value_i)
                else:
                    printf("未输入染色体类，无法识别并使用")
            self.__length = len(self.__chromosome_result)
        else:
            printf("未输入物种初始列表，无法识别并使用")

    @property
    def length(self):
        return self.__length

    @length.setter
    def length(self, value):
        self.__length = len(self.chromosome_result)

    @property
    def static_value(self):
        return self.__static_value

    @static_value.setter
    def static_value(self, value):
        if value is None:
            self.__static_value = list()
        elif isinstance(value, Gene):
            self.__static_value = [value]
        elif isinstance(value, (tuple, list)):
            self.__static_value = list()
            for value_i in value:
                if isinstance(value_i, Gene):
                    self.__static_value.append(value_i)
                else:
                    printf("static_value不是Gene或list/tuple类型，无法加载")
        else:
            printf("static_value不是Gene或list/tuple类型，无法加载")
            self.__static_value = list()

    def __str__(self):
        return " | ".join(list(map(
            lambda x: str(x), self.chromosome_result
        )))

    def __repr__(self):
        return self.__str__()

    def run(self):
        self.chromosome_best_result_list = list()
        for i in range(0, self.maxItem):
            self.inheritance()
            self.eliminate()
            print("第%d次迭代已结束，共%d个" % ((i + 1), self.length))
            # print("Result:", self)

    def inheritance(self):
        children = list()
        for i in range(0, self.length * self.group_times):
            father = self.chromosome_result[random.randint(0, self.length - 1)]
            mother = self.chromosome_result[random.randint(0, self.length - 1)]
            children.extend(father.crisscross_inheritance(father, mother, self.group_times, True, self.mutation_pro))
        self.chromosome_result.extend(children)
        self.length = True

    def eliminate(self):
        chromosome_estimate = list(map(lambda x: x.estimate(*self.static_value), self.chromosome_result))
        sum_estimate = sum(chromosome_estimate)
        choose = random.sample(range(int(sum_estimate)), round(self.length * (1 - self.elimination_rate)))
        self.chromosome_result = [
            self.chromosome_result[randint_choose(chromosome_estimate, choose_i)] for choose_i in choose
        ]
        self.length = True

    def get_best_result(self, num: int = 1):
        if self.chromosome_best_result_list:
            pass
        else:
            self.chromosome_best_result_list = list(set(self.chromosome_result))
            self.chromosome_best_result_list.sort(key=lambda c: c.estimate(*self.static_value), reverse=True)
        return list(map(
            lambda x: x.add_static_gene(*self.static_value), self.chromosome_best_result_list[:num]
        ))


hero_estimate_dict = {
}
for key in [1, 2, 3, 4, 5]:
    hero_estimate_dict[key] = random.randint(1, 10)


def hero_estimate(hero_id):
    return hero_estimate_dict[hero_id] if hero_id in hero_estimate_dict else 0


if __name__ == '__main__':
    Gene_input_set = Gene(maxValue=10, key_create_method=hero_estimate)
    test = Gene_input_set.create_gene(5)
    print(test.estimate())
    Chromosome_input_set = Chromosome()
    Chromosome_input_set.gene_template = Gene_input_set
    Chromosome_input_set.set_gene_list(*[3, 4, 5, 6, 7])
    print(Chromosome_input_set.estimate())
    Chromosome_group = []
    Chromosome_group += [
        Chromosome_input_set.create_chromosome(*[3, 4, 5, 6, 7]),
        Chromosome_input_set.create_chromosome(*[3, 4, 5, 6, 7]),
        Chromosome_input_set.create_chromosome(*[3, 4, 5, 6, 7])]
    GA_result = GA(
        *Chromosome_group,
        maxItem=10,
        min_threshold=0,
        max_threshold=100,
        elimination_rate=0.55,
        group_times=1,
        mutation_pro=0.1,
        static_value=Gene_input_set.create_gene(6)
    )
    GA_result.run()
    xxx = GA_result.get_best_result(10)
    printf(xxx)
