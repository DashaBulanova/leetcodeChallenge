#
# class MultiKeyDict:
#     first_key = Dict[int, int]
#     second_key = Dict[int, int]
#
#     def add(self, first_key, second_key, value):
#         if (first_key)

class CacheRow:
    min: int
    max: int
    values: dict[int, int]

    def __init__(self, index):
        self.min = index

    def add_acc(self, index, value):
        self.values[index] = value
        if

            df.withColumn('prc_cases', df['total_cases_per_million'].cast(FloatType()))\
                .select(['iso_code', 'location', 'date', 'total_cases_per_million', 'prc_cases'])\
                .where('date=="2020-03-31"').sort(col('prc_cases').desc()).show(15)

            res = df.filter(df['date'] == '2021-03-31') \
                .select('iso_code',
                        'location',
                        round(col('total_cases_per_million') / 10_000, 2).alias('recovered_percent ')) \
                .orderBy(col('total_cases_per_million').desc())


class NumArray:

    def __init__(self, nums: list[int]):
        if nums is None:
            raise ValueError("argument null exception")
        self.__nums = nums
        self.__cache = dict[int, CacheRow]

    # def get_key(self, left: int, right: int):
    #     return f"{left}:{right}"
    #
    # def __check_key(self, left: int, right: int):
    #     return self.__cache.get(self.get_key(left, right))

    def sumRange(self, left: int, right: int) -> int:
        if not (0 <= left <= right < len(self.__nums)):
            raise ValueError("0 <= left <= right < len(self.__nums violation")

        acc = 0
        for i in range(left, right+1):
            acc += self.__nums[i]
            self.__cache[left][right] = acc

        return acc
