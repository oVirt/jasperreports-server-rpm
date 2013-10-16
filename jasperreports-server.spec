%global product_description JasperReports Server
%global install_poms 1

%global jrs_name jasperreports-server

Name: jasperreports-server
Version: 5.2.0
Release: 1
License: AGPLv3
Summary: %{product_name}
Group: Virtualization/Management
URL: http://community.jaspersoft.com
BuildArchitectures: noarch
Source: http://downloads.sourceforge.net/project/jasperserver/JasperServer/JasperReports%20Server%20%{version}/%{name}-cp-%{version}-bin.zip

BuildRequires: java-1.7.0-openjdk-devel
Requires: bash
Requires: java
Requires: postgresql-jdbc
Requires: postgresql-server >= 8.4.7
Requires: postgresql-contrib >= 8.4.7
# Require JBoss EAP 6:
Requires: jboss-annotations-1.1-api
Requires: jboss-ejb-3.1-api
Requires: jboss-logging
Requires: jboss-servlet-3.0-api
Requires: jboss-logging
Requires: jboss-as >= 7.1.1
Requires: jboss-interceptors-1.1-api

%description
%{product_description} is a powerful, yet flexible and
lightweight reporting server. Generate, organize, secure,
and deliver interactive reports and dashboards to users.
Allow non-technical users to build their own reports and
dashboards.

%prep
%setup -c -q

%install
install -d %{buildroot}%{_datadir}/%{name}
cp -r %{name}-cp-%{version}-bin/* %{buildroot}%{_datadir}/%{name}

%files
%defattr(-,root,root,-)
%{_datadir}/%{name}

%changelog
* Tue Sep 24 2013 Yaniv Dary <ydary@redhat.com> - 5.2.0
Update to 5.2.0.

* Sun Jun 10 2012 Yaniv Dary <ydary@redhat.com> - 4.7.0
- inital commit
