from demo1.source_code.run import RunTest

runner = RunTest()
# 实例化多个进程，进程数为4
filenames = runner.getExcel()       #获取测试用例，并作为迭代对象
runner.runPool(func=runner.runTest,iterable=filenames,threads_num=1)