PORTNAME=	veil
DISTVERSION=	297.d8acd4c
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	A tool designed to generate metasploit payloads that bypass common anti-virus solutions.
WWW=		https://github.com/Veil-Framework/Veil

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git

RUN_DEPENDS=	??/ca-certificates \
		??/capstone \
		??/metasploit \
		??/mingw-w64-binutils \
		??/mingw-w64-crt \
		??/mingw-w64-gcc \
		??/mingw-w64-headers \
		??/mingw-w64-winpthreads \
		??/mono \
		??/mono-tools \
		??/py-capstone@${PY_FLAVOR} \
		??/py-pefile@${PY_FLAVOR} \
		??/py-pycryptodome@${PY_FLAVOR} \
		??/pyinstaller \
		??/sudo \
		??/wine-mono \
		??/wine_gecko \
		archivers/unzip \
		devel/git \
		devel/py-pip@${PY_FLAVOR} \
		emulators/wine \
		ftp/wget \
		lang/python \
		lang/ruby


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
