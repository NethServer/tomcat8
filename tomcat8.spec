Summary: Tomcat 8
Name: tomcat8
Version: 8.5.34
Release: 1%{?dist}
License: GPL
URL: %{url_prefix}/%{name} 
Source0: http://it.apache.contactlab.it/tomcat/tomcat-8/v%{version}/bin/apache-tomcat-%{version}.tar.gz
Source1: tomcat8.service
Source2: tomcat8@.service

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
# add the tomcat user and group
getent group tomcat >/dev/null || /usr/sbin/groupadd -f -g 53 -r tomcat
if ! getent passwd tomcat >/dev/null ; then
    if ! getent passwd 53 >/dev/null ; then
        /usr/sbin/useradd -r -u 53 -g tomcat -d /usr/share/tomcat -s /sbin/nologin -c "Apache Tomcat" tomcat
        # Tomcat uses a reserved ID, so there should never be an else
    fi
fi
exit 0

%description
Tomcat 8 binary

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/opt/tomcat8
tar xvf  %{SOURCE0} -C %{buildroot}/opt/tomcat8 --strip-components=1
mkdir -p %{buildroot}/usr/lib/systemd/system/
cp %{SOURCE1} %{buildroot}/usr/lib/systemd/system/
cp %{SOURCE2} %{buildroot}/usr/lib/systemd/system/
rm -rf %{buildroot}/opt/tomcat8/webapps/examples


%files
%defattr(-,root,tomcat)
/usr/lib/systemd/system/*
/opt/tomcat8/lib/*
/opt/tomcat8/bin/*
%doc /opt/tomcat8/BUILDING.txt
%doc /opt/tomcat8/CONTRIBUTING.md
%doc /opt/tomcat8/LICENSE
%doc /opt/tomcat8/NOTICE
%doc /opt/tomcat8/README.md
%doc /opt/tomcat8/RELEASE-NOTES
%doc /opt/tomcat8/RUNNING.txt
%attr(0770, tomcat, tomcat)/opt/tomcat8/webapps
%attr(0770, tomcat, tomcat)/opt/tomcat8/work
%attr(0770, tomcat, tomcat)/opt/tomcat8/temp
%attr(0770, tomcat, tomcat)/opt/tomcat8/logs
%attr(0770, tomcat, tomcat)/opt/tomcat8/conf

%changelog
