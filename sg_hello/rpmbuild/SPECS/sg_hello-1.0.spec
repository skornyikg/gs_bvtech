Name: sg_hello
Version: 1 
Release: 0 
Summary: HelloWorld 
Packager: Gabor Skornyik
Group: Application/Other 
License: GPL 
Source0: %{name}-%{version}.tar.gz 
BuildArch: noarch 

%description
HelloWorld

%prep 
%setup -q 

%build 

%install 
rm -rf $RPM_BUILD_ROOT 
mkdir -p $RPM_BUILD_ROOT/usr/local/sbin 
cp scripts/* $RPM_BUILD_ROOT/usr/local/sbin/ 

%clean 
rm -rf $RPM_BUILD_ROOT 

%files 
%defattr(-,root,root,-) 
%dir 
/usr/local/sbin 
/usr/local/sbin/sg_hello

%doc 
%changelog * 1.0 - initial release

