import logging
logging.basicConfig(level=logging.INFO)
import subprocess
import datetime

logger = logging.getLogger(__name__)
news_sites_uids = ['eluniversal', 'eltiempo']


def main():
	_extract()
	_transform()
	_load()


def _extract():
	logger.info('Starting extract process')
	for news_site_uid in news_sites_uids:
		subprocess.run(['python', 'main.py', news_site_uid], cwd='./extract') #ejecutamos nuestro web scraper por cada uno de nuestros sitios de noticias, #mover (mv) los archivos que se generaron. exec-ejecute algo por cada archivo que encuentre
		subprocess.run(['copy', r'H:\Platzi\Ingenieria_de_datos\extract\*.csv', r'H:\Platzi\Ingenieria_de_datos\transform'], shell=True)#, cwd='./extract')
	

def _transform():
	logger.info('Starting transform process')
	for news_site_uid in news_sites_uids:
		now = datetime.datetime.now().strftime('%Y_%m_%d')
		dirty_data_filename = '{news_site_uid}_{datetime}_articles.csv'.format(news_site_uid=news_site_uid, datetime=now)
		clean_data_filename = 'clean_{}'.format(dirty_data_filename)
		subprocess.run(['python', 'main.py', dirty_data_filename], cwd='./transform') #ejecutamos nuestro programa de transform
		subprocess.run(['del', dirty_data_filename], shell=True, cwd='./transform')
		subprocess.run(['copy', r'H:\Platzi\Ingenieria_de_datos\transform\*.csv', r'H:\Platzi\Ingenieria_de_datos\load'
                        ], shell=True) #cwd='./transform')        


def _load():
	logger.info('Starting load process')
	for news_site_uid in news_sites_uids:
		now = datetime.datetime.now().strftime('%Y_%m_%d')
		clean_data_filename = 'clean_{news_site_uid}_{datetime}_articles.csv'.format(news_site_uid=news_site_uid, datetime=now)
		subprocess.run(['python', 'main.py', clean_data_filename], cwd='./load')
		#subprocess.run(['rm',clean_data_filename], cwd='./load')

if __name__ == '__main__':
	main()