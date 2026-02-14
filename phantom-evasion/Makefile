PORTNAME=	phantom-evasion
DISTVERSION=	103.2cd0673
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Antivirus evasion tool written in python.
WWW=		https://github.com/oddcod3/Phantom-Evasion

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git

RUN_DEPENDS=	??/dex2jar \
		??/gcc-multilib \
		??/metasploit \
		??/mingw-w64-binutils \
		??/mingw-w64-gcc \
		??/py-pyopenssl@${PY_FLAVOR} \
		??/sign \
		lang/python


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
