Name:           ros-lunar-slime-ros
Version:        0.4.12
Release:        0%{?dist}
Summary:        ROS slime_ros package

Group:          Development/Libraries
License:        Public Domain
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-lunar-rosemacs
Requires:       ros-lunar-roslisp
Requires:       ros-lunar-slime-wrapper
Requires:       sbcl
BuildRequires:  ros-lunar-catkin

%description
Extensions for slime to assist in working with ROS packages

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/lunar/setup.sh" ]; then . "/opt/ros/lunar/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/lunar" \
        -DCMAKE_PREFIX_PATH="/opt/ros/lunar" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/lunar/setup.sh" ]; then . "/opt/ros/lunar/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/lunar

%changelog
* Fri Mar 16 2018 Gayane Kazhoyan <kazhoyan@cs.uni-bremen.de> - 0.4.12-0
- Autogenerated by Bloom

* Thu May 04 2017 Gayane Kazhoyan <kazhoyan@cs.uni-bremen.de> - 0.4.11-0
- Autogenerated by Bloom

