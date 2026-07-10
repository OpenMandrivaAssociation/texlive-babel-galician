%global tl_name babel-galician
%global tl_revision 30270

Name:		texlive-%{tl_name}
Epoch:		1
Version:	4.3c
Release:	%{tl_revision}.1
Summary:	Babel/Polyglossia support for Galician
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/babel-contrib/galician
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/babel-galician.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/babel-galician.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/babel-galician.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
Requires(pre):	texlive-tlpkg
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package provides a language description file that enables support of
Galician either with babel or with polyglossia.

%prep
%setup -q -c -a1 -a2
rm -rf tlpkg
if [ -d RELOC ]; then
	cp -a RELOC/. .
	rm -rf RELOC
fi

%build

%install
mkdir -p %{buildroot}%{_datadir}/texmf-dist
# Flat tlnet layout: tex/ doc/ source/ fonts/ ... -> texmf-dist/
if [ -d texmf-dist ]; then
	cp -a texmf-dist/. %{buildroot}%{_datadir}/texmf-dist/
elif [ -d texmf ]; then
	mkdir -p %{buildroot}%{_datadir}/texmf
	cp -a texmf/. %{buildroot}%{_datadir}/texmf/
else
	for d in * .[!.]* ..?*; do
		[ -e "$d" ] || continue
		case "$d" in tlpkg|RELOC) continue ;; esac
		cp -a "$d" %{buildroot}%{_datadir}/texmf-dist/
	done
fi
rm -rf %{buildroot}%{_datadir}/texmf-dist/tlpkg

%files
%dir %{_datadir}/texmf-dist
%dir %{_datadir}/texmf-dist/doc
%dir %{_datadir}/texmf-dist/source
%dir %{_datadir}/texmf-dist/tex
%dir %{_datadir}/texmf-dist/doc/generic
%dir %{_datadir}/texmf-dist/source/generic
%dir %{_datadir}/texmf-dist/tex/generic
%dir %{_datadir}/texmf-dist/doc/generic/babel-galician
%dir %{_datadir}/texmf-dist/source/generic/babel-galician
%dir %{_datadir}/texmf-dist/tex/generic/babel-galician
%doc %{_datadir}/texmf-dist/doc/generic/babel-galician/galician.pdf
%doc %{_datadir}/texmf-dist/doc/generic/babel-galician/glbst.tex
%doc %{_datadir}/texmf-dist/doc/generic/babel-galician/glromidx.tex
%doc %{_datadir}/texmf-dist/source/generic/babel-galician/galician.dtx
%doc %{_datadir}/texmf-dist/source/generic/babel-galician/galician.ins
%{_datadir}/texmf-dist/tex/generic/babel-galician/galician.ldf
