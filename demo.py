# # BELOW CODE IS TI CHECK LOGGING CONFIG
# from src.logger import logging
# logging.debug("This is a debug message")
# logging.info("This is an info message")
# logging.warning("This is an warning message")
# logging.error("This is an error message")
# logging.critical("This is an critical message")


# # BELOW CODE IS TO CHECK THE EXCEPTION CONFIG
# from src.logger import logging
# from src.exception import MyException
# import sys
# try:
#     a = 1+'Z'
# except Exception as e:
#     logging.info(e)
#     raise MyException(e , sys) from e


from src.pipline.training_pipeline import TrainPipeline
pipline = TrainPipeline()
pipline.run_pipeline()