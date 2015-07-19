# revision 27034
# category Package
# catalog-ctan /macros/latex/contrib/footnotebackref
# catalog-date 2012-07-05 10:27:55 +0200
# catalog-license lppl1.3
# catalog-version 1.0
Name:		texlive-footnotebackref
Version:	1.0
Release:	9
Summary:	Back-references from footnotes
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/footnotebackref
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/footnotebackref.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/footnotebackref.doc.tar.xz
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
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}


%changelog
* Thu Aug 09 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.0-1
+ Revision: 813494
- Import texlive-footnotebackref
- Import texlive-footnotebackref

