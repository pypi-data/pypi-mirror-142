from data_quality_check.config import ConfigProfilingGeneral, ConfigDataset, ConfigProfilingCustomized, Config
from data_quality_check.profiler.customized_profiler import CustomizedProfilerResult, CustomizedProfiler
from data_quality_check.profiler.general_profiler import GeneralProfilerResult, GeneralProfiler


class CombinedProfilerResult:
    spark: None
    general_profiler_result: GeneralProfilerResult = None
    customized_profiler_result: CustomizedProfilerResult = None

    def __init__(self, spark, general_profiler_result, customized_profiler_result):
        self.spark = spark
        self.general_profiler_result = general_profiler_result
        self.customized_profiler_result = customized_profiler_result


class CombinedProfiler:
    dataset_config: ConfigDataset = None
    general_profiling_config: ConfigProfilingGeneral = None
    customized_profiling_config: ConfigProfilingCustomized = None

    general_profiler_result: GeneralProfilerResult = None
    customized_profiler_result: CustomizedProfilerResult = None

    def __init__(self, spark, config: Config = None, dataset_config: ConfigDataset = None,
                 general_profiling_config: ConfigProfilingGeneral = ConfigProfilingGeneral(),
                 customized_profiling_config: ConfigProfilingCustomized = None):
        self.spark = spark
        if config is not None:
            self.dataset_config = config.dataset
            self.general_profiling_config = config.profiling.general
            self.customized_profiling_config = config.profiling.customized
        else:
            self.dataset_config = dataset_config
            self.general_profiling_config = general_profiling_config
            self.profiling_config = customized_profiling_config

    def run(self):
        if self.general_profiling_config is not None:
            general_profiler = GeneralProfiler(self.spark,
                                               config=self.general_profiling_config,
                                               dataset_config=self.dataset_config)
            self.general_profiler_result = general_profiler.run(return_type='profile_result')

        if self.customized_profiling_config is not None:
            customized_profiler = CustomizedProfiler(self.spark, dataset_config=self.dataset_config,
                                                     customized_profiling_config=self.customized_profiling_config)
            self.customized_profiler_result = customized_profiler.run(return_type='profile_result')

        return CombinedProfilerResult(spark=self.spark, general_profiler_result=self.general_profiler_result,
                                      customized_profiler_result=self.customized_profiler_result)
