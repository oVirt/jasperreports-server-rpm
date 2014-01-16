Name: jasperreports-server
Version: 5.5.0
Release: 2%{?dist}
License: AGPLv3
Summary: JasperReports Server
URL: http://community.jaspersoft.com
BuildArch: noarch
Source: http://downloads.sourceforge.net/project/jasperserver/JasperServer/JasperReports%20Server%20Community%20Edition%20%{version}/%{name}-cp-%{version}-bin.zip

AutoReqProv: no
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
JasperReports Server is a powerful, yet flexible and
lightweight reporting server. Generate, organize, secure,
and deliver interactive reports and dashboards to users.
Allow non-technical users to build their own reports and
dashboards.

%prep
%setup -c -q

%build

%install
install -d %{buildroot}%{_datadir}/%{name}
cp -r %{name}-cp-%{version}-bin/* %{buildroot}%{_datadir}/%{name}

%files
%defattr(-,root,root,-)
%{_datadir}/%{name}

%changelog

* Fri Dec 20 2013 Sandro Bonazzola <sbonazzo@redhat.com> - 5.5.0-2
- Fixed W: no-build-section
- Fixed W: invalid-url

* Wed Nov 13 2013 Yaniv Dary <ydary@redhat.com> - 5.5.0-1
- Update to 5.5.0.

* Tue Sep 24 2013 Yaniv Dary <ydary@redhat.com> - 5.2.0
- Update to 5.2.0.

* Sun Jun 10 2012 Yaniv Dary <ydary@redhat.com> - 4.7.0
- inital commit
