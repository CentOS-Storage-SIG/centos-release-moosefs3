Summary: MooseFS 3 packages from the CentOS Storage SIG repository
Name: centos-release-moosefs3
Version: 0.9
Release: 1%{?dist}
License: GPLv2
URL: http://wiki.centos.org/SpecialInterestGroup/Storage
Source0: CentOS-MooseFS-3.repo
BuildArch: noarch

%if 0%{?centos} >= 7
# $contentdir for altarch support was added with CentOS-7.5
Requires: centos-release >= 7-5.1804.el7.centos.2
%endif
# This provides the public key to verify the RPMs
Requires: centos-release-storage-common

Provides: centos-release-moosefs = 3

%description
yum configuration for MooseFS 3 packages from the CentOS Storage SIG.

%install
install -D -m 644 %{SOURCE0} %{buildroot}%{_sysconfdir}/yum.repos.d/CentOS-MooseFS-3.repo
%if 0%{?centos} < 7
sed -i 's/i\$contentdir/centos/g' %{buildroot}%{_sysconfdir}/yum.repos.d/CentOS-MooseFS-3.repo
%endif

%files
%defattr(-,root,root)
%config(noreplace) %{_sysconfdir}/yum.repos.d/CentOS-MooseFS-3.repo

%changelog
* Tue Jun 25 2019 Niels de Vos <ndevos@redhat.com> - 0.9-1
- Initial version based on centos-release-gluster6
- Only the centos-moosefs3-test repo is enabled during pre-release
