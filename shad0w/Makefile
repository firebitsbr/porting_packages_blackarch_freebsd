PORTNAME=	shad0w
DISTVERSION=	387.d35b9dc
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	A modular C2 framework designed to successfully operate on mature environments.
WWW=		https://github.com/bats3c/shad0w

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git \
		devel/py-setuptools@${PY_FLAVOR}

RUN_DEPENDS=	??/donut \
		??/dotnet-sdk \
		??/metasploit \
		??/mingw-w64-gcc \
		??/mono \
		??/nasm \
		??/py-cffi@${PY_FLAVOR} \
		??/py-flask@${PY_FLAVOR} \
		??/py-pefile@${PY_FLAVOR} \
		??/py-prettytable@${PY_FLAVOR} \
		??/py-prompt_toolkit@${PY_FLAVOR} \
		??/py-pygments@${PY_FLAVOR} \
		??/py-pyopenssl@${PY_FLAVOR} \
		??/upx \
		lang/python \
		www/py-requests@${PY_FLAVOR}


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
