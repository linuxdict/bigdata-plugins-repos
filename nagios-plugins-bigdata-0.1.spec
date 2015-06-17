Name:           nagios-linuxdict-plugins
Version:        0.1
Release:        1
Summary:        Nagios plugins for hadoop/hbase and so , packed by edy@linuxdict.com
Group:          System Environment/Libraries
License:        GPL
Requires:       python-pymongo,glibc-devel,perl-Class-Accessor,perl-common-sense,perl-Compress-Raw-Zlib,perl-Data-Dumper-Names,perl-DBD-MySQL,perl-DBI,perl-devel,perl-Digest-HMAC,perl-Digest-SHA1,perl-Digest-SHA,perl-Expect,perl-ExtUtils-MakeMaker,perl-ExtUtils-ParseXS,perl-GSSAPI,perl-HTML-Parser,perl-HTML-Tagset,perl-IO-Compress-Base,perl-IO-Compress-Zlib,perl-IO-Socket-Timeout,perl-IO-Tty,perl-JSON,perl-JSON-XS,perl-libwww-perl,perl-LWP-Authen-Negotiate,perl-Net-DNS,perl-Net-SSH-Expect,perl-PadWalker,perl-PerlIO-via-Timeout,perl-Readonly,perl-Readonly-XS,perl-Redis,perl-Test-Harness,perl-Test-SharedFork,perl-Test-Simple,perl-Time-HiRes,perl-Try-Tiny,perl-URI,perl-XML-Parser,perl-XML-Simple,php-channel-horde,php-cli,php-common,php-horde-Horde-Thrift,php-pear
Source0:        %{name}-%{version}.tar.gz
BuildRoot:      %{_topdir}/BUILDROOT 

%description

%prep

%setup -q

%install
mkdir -p %{buildroot}/usr/local/nagios/libexec/ 
mkdir -p %{buildroot}/usr/local/nagios/etc/nrpe_local/
cp check* %{buildroot}/usr/local/nagios/libexec/ 
cp etc/*.cfg %{buildroot}/usr/local/nagios/etc/nrpe_local/
mkdir -p %{buildroot}/usr/lib64/perl5/vendor_perl/
mkdir -p %{buildroot}/usr/local/lib64/perl5/auto/Net/ZooKeeper/
cp -R lib/*  %{buildroot}/usr/lib64/perl5/vendor_perl/
cp -R auto %{buildroot}/usr/local/lib64/perl5/
cp usr/lib64/libzookeeper_mt.so.2 %{buildroot}/usr/lib64/
rm -rf %{buildroot}/usr/lib64/perl5/vendor_perl/HariSekhon/HBase/Thrift.pm
rm -rf %{buildroot}/usr/lib64/perl5/vendor_perl/HariSekhon/MongoDB.pm
rm -rf %{buildroot}/usr/lib64/perl5/vendor_perl/Hbase/Hbase.pm
rm -rf %{buildroot}/usr/lib64/perl5/vendor_perl/Hbase/Types.pm
rm -rf %{buildroot}/usr/lib64/perl5/vendor_perl/Hbase/Constants.pm
rm -rf %{buildroot}/usr/lib64/perl5/vendor_perl/{LICENSE,Makefile,README.md,testcmd.exp}
rm -rf %{buildroot}/usr/lib64/perl5/vendor_perl/t
rm -rf %{buildroot}/usr/lib64/perl5/vendor_perl/Net/.exists


%files    
%defattr(-,nagios,nagios,-)
 /usr/lib64/perl5/vendor_perl/HariSekhon/Ambari.pm
 /usr/lib64/perl5/vendor_perl/HariSekhon/Cassandra.pm
 /usr/lib64/perl5/vendor_perl/HariSekhon/Cassandra/Nodetool.pm
 /usr/lib64/perl5/vendor_perl/HariSekhon/ClouderaManager.pm
 /usr/lib64/perl5/vendor_perl/HariSekhon/DataStax/OpsCenter.pm
 /usr/lib64/perl5/vendor_perl/HariSekhon/Datameer.pm
 /usr/lib64/perl5/vendor_perl/HariSekhon/ElasticSearch.pm
 /usr/lib64/perl5/vendor_perl/HariSekhon/HBase.pm
 /usr/lib64/perl5/vendor_perl/HariSekhon/IBM/BigInsights.pm
 /usr/lib64/perl5/vendor_perl/HariSekhon/MapR.pm
 /usr/lib64/perl5/vendor_perl/HariSekhon/Redis.pm
 /usr/lib64/perl5/vendor_perl/HariSekhon/ZooKeeper.pm
 /usr/lib64/perl5/vendor_perl/HariSekhonUtils.pm
 /usr/lib64/perl5/vendor_perl/HariSekhonUtils.py
 /usr/lib64/perl5/vendor_perl/HariSekhonUtils.pyc
 /usr/lib64/perl5/vendor_perl/HariSekhonUtils.pyo
 /usr/lib64/perl5/vendor_perl/Net/*
 /usr/local/lib64/perl5/auto/Net/ZooKeeper/*
 /usr/local/nagios/libexec/*
 /usr/lib64/libzookeeper_mt.so.2
 /usr/local/nagios/etc/nrpe_local/*

%post
if [ -f /etc/init.d/opsview-agent ] ; then
  /etc/init.d/opsview-agent stop
  /etc/init.d/opsview-agent start
fi
