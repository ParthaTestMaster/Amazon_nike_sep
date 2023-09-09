### how to customise loggers ########3
### we are not using from looger import logging, beacuse logging is in built module  in python, just import.
import inspect
import logging

class cutlogger(self, logLevel=logging.DEBUG):

        # 'application' code
        logger.debug('debug message')
        logger.info('info message')
        logger.warning('warn message')
        logger.error('error message')
        logger.critical('critical message')


lg = LoggerDemo()   ## call the sample_logger() function.
lg.sample_logger()










# import logging
#
# # create logger
# logger = logging.getLogger('simple_example')
# logger.setLevel(logging.DEBUG)
#
# # create console handler and set level to debug
# ch = logging.StreamHandler()
# ch.setLevel(logging.DEBUG)
#
# # create formatter
# formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
#
# # add formatter to ch
# ch.setFormatter(formatter)
#
# # add ch to logger
# logger.addHandler(ch)
#
# # 'application' code
# logger.debug('debug message')
# logger.info('info message')
# logger.warning('warn message')
# logger.error('error message')
# logger.critical('critical message')


# ###### simple logger codes############
# import logging
# logging.basicConfig(level=logging.DEBUG, filename='../logs/demologs.log', filemode='w', format='%(asctime)s-%(levelname)s-%(message)s')
# ## filemode = append(a), write(w)
#
# logging.debug('This is a debug message')
# logging.info('This is an info message')
# logging.warning('This is a warning message')
# logging.error('This is an error message')
# logging.critical('This is a critical message')

