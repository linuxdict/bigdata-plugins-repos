# bigdata-plugins-repos
hadoop monitor plugins for RH's, can build to rpms packages

# Install the plugin
Notes: Tested on CentOS 6.x 64bit

yum localinstall nagios-linuxdict-plugins-0.1-1.x86_64.rpm

# Rebuild by yourself
rpmbuild -ba nagios-plugins-bigdata-0.0.2.spec
