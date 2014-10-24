Name:           essentials
Version:        0.0.5
Release:        0%{?dist}
Summary:        Essential scripts for lazy things

License:        GPLv3
URL:            https://github.com/sri-arjuna/%{name}
Source0:        %{name}-%{version}.tar.gz

Requires:       tui


%description
backup-config
blame
chx
compile
dl-fed
dracut-rebuild
export-script
go_rawhide
hdmi
nvidia
p
pm
rmtf
rnd
screenshot
siggen

%prep
%setup -q -c %{name}-%{version}

%build
# Nothing to do

%install
rm -rf $RPM_BUILD_ROOT
##%make_install

mkdir -p %{buildroot}%{_bindir}/ \
         %{buildroot}%{_datarootdir}/%{name}
rm -fr %{name}/.git
rm -fr build-rpm-essentials.sh
mv %{name}/bin/* %{buildroot}%{_bindir}/
mv %{name}/[RL]*  %{buildroot}%{_datarootdir}/%{name}

%files
%doc %{_datarootdir}/%{name}/README.md 
%doc %{_datarootdir}/%{name}/LICENSE
%{_bindir}/backup-config
%{_bindir}/blame
%{_bindir}/chx
%{_bindir}/compile
%{_bindir}/dl-fed
%{_bindir}/dracut-rebuild
%{_bindir}/export-script
%{_bindir}/go_rawhide
%{_bindir}/hdmi
%{_bindir}/nvidia
%{_bindir}/p
%{_bindir}/pm
%{_bindir}/rmtf
%{_bindir}/rnd
%{_bindir}/screenshot
%{_bindir}/siggen

%changelog
* Fri Oct 24 2014 Simon A. Erat <erat.simon@gmail.com> 0.0.5
- Initial package
