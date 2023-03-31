Name:		texlive-footnotebackref
Version:	27034
Release:	2
Summary:	Back-references from footnotes
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/footnotebackref
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/footnotebackref.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/footnotebackref.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package provides the means of creating hyperlinks, from a
footnote at the bottom of the page, back to the occurence of
the footnote in the main text.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/footnotebackref/footnotebackref.sty
%doc %{_texmfdistdir}/doc/latex/footnotebackref/README
%doc %{_texmfdistdir}/doc/latex/footnotebackref/footnotebackref.pdf
%doc %{_texmfdistdir}/doc/latex/footnotebackref/footnotebackref.tex

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
