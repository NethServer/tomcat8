Summary: Tomcat 8
Name: tomcat8
Version: 8.5.34
Release: 1%{?dist}
License: GPL
URL: %{url_prefix}/%{name} 
Source0: http://it.apache.contactlab.it/tomcat/tomcat-8/v%{version}/bin/apache-tomcat-%{version}.tar.gz
Source1: tomcat8.service

Requires: java-1.8.0-openjdk, apache-commons-daemon-jsvc

Requires(pre): shadow-utils
%{?systemd_requires}
BuildRequires: systemd

%post
%systemd_post tomcat8.service

%preun
%systemd_preun tomcat8.service

%postun
%systemd_postun_with_restart tomcat8.service

# Disable debuginfo creation
%define debug_package %{nil}

%pre
getent group tomcat8 >/dev/null || groupadd -r tomcat8
getent passwd tomcat8 >/dev/null || \
    useradd -r -g tomcat8 -d /opt/tomcat8 -s /sbin/nologin \
    -c "Apache Tomcat 8" tomcat8
exit 0

%description
Tomcat 8 binary

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/opt/tomcat8
tar xvf  %{SOURCE0} -C %{buildroot}/opt/tomcat8 --strip-components=1
mkdir -p %{buildroot}/usr/lib/systemd/system/
cp %{SOURCE1} %{buildroot}/usr/lib/systemd/system/


%files
%defattr(-,root,tomcat8)
/usr/lib/systemd/system/tomcat8.service
/opt/tomcat8/lib/*
/opt/tomcat8/bin/*
%doc /opt/tomcat8/BUILDING.txt
%doc /opt/tomcat8/CONTRIBUTING.md
%doc /opt/tomcat8/LICENSE
%doc /opt/tomcat8/NOTICE
%doc /opt/tomcat8/README.md
%doc /opt/tomcat8/RELEASE-NOTES
%doc /opt/tomcat8/RUNNING.txt
%attr(0770, tomcat8, tomcat8)/opt/tomcat8/webapps
%attr(0770, tomcat8, tomcat8)/opt/tomcat8/work
%attr(0770, tomcat8, tomcat8)/opt/tomcat8/temp
%attr(0770, tomcat8, tomcat8)/opt/tomcat8/logs
%attr(0770, tomcat8, tomcat8)/opt/tomcat8/conf

%changelog
