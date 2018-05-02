import jenkins
#import config

server = jenkins.Jenkins('http://nalxd.eastus.cloudapp.azure.com:8080', username='gkadmin', password='88917c31df89cb726ccc6a59077731bb')
#plugins = server.get_plugins_info()
#print plugins

#jobs = server.get_job_info( name='NEWJOB' )
#jobsinfo = server.get_job_info( 'NEWJOB', depth=2, fetch_all_builds=True )
#jobsinfo = server.get_jobs(  )
jobsinfo = server.build_job( name='expipeline')
print jobsinfo
#serverbuild_job(name, parameters=None, token=None)
#print jobsinfo['lastSuccessfulBuild']['url']
#print len(jobsinfo)
#print dir(jobsinfo)
#print(jobsinfo).['lastSuccessfulBuild']
#print config.STG_INT

#user = server.get_whoami()
#ersion = server.get_version()
#print user
#print version
#print('Hello %s from Jenkins %s' % (user['fullName'], version))
