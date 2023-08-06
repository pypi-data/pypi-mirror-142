"""
字符串随机编码方案。编码后保持字符串的相对排序不变，允许局部搜索。
"""
import time
import string
from fastutils import cipherutils


class SrndCipher(cipherutils.MappingCipher):

    default_result_encoder = cipherutils.Utf8Encoder()

    """字符串随机编码方案。编码后保持字符串的相对排序不变，允许局部搜索。
    """
    def __init__(self, password, seed_min_length=2, seed_max_length=11, chars=string.ascii_letters + string.digits + string.punctuation, **kwargs):
        self.seed_min_length = seed_min_length
        self.seed_max_length = seed_max_length
        self.chars = chars
        self.get_seeds_loop_counter = 0
        stime = time.time()
        super().__init__(password, **kwargs)
        self.get_seeds_time_used = time.time() - stime

    def get_seeds(self):
        seeds = set()
        bad_seeds = set()
        while True:
            self.get_seeds_loop_counter += 1
            length = self.randomGenerator.randint(self.seed_min_length, self.seed_max_length)
            seed = "".join(self.randomGenerator.choices(self.chars, k=length))
            if self.test_seed(seeds, bad_seeds, seed):
                self.put_bad_seeds(bad_seeds, seeds, seed)
                seeds.add(seed)
            if len(seeds) >= 256:
                break
        seeds = list([x.encode() for x in seeds])
        seeds.sort()
        return seeds

    def test_seed(self, seeds, bad_seeds, seed):
        if seed in bad_seeds:
            return False
        for x in bad_seeds:
            if x in seed:
                return False
            if seed in x:
                return False
        new_bad_seeds = set()
        for x in seeds:
            new_bad_seeds.add(x[-1] + seed[0])
            new_bad_seeds.add(seed[-1] + x[0])
        for x in new_bad_seeds:
            for y in seeds:
                if x in y:
                    return False
        return True

    def put_bad_seeds(self, bad_seeds, seeds, seed):
        bad_seeds.add(seed)
        bad_seeds.add(seed[-1] + seed[0])
        for x in seeds:
            bad_seeds.add(seed[-1] + x[0])
            bad_seeds.add(x[-1] + seed[0])
