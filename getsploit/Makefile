PORTNAME=	getsploit
DISTVERSION=	v2.0.2.r0.gb7a4a8e
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Command line utility for searching and downloading exploits.
WWW=		https://github.com/vulnersCom/getsploit

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	??/py-build@${PY_FLAVOR} \
		??/py-installer@${PY_FLAVOR} \
		??/py-wheel@${PY_FLAVOR} \
		devel/git \
		devel/py-pip@${PY_FLAVOR} \
		devel/py-setuptools@${PY_FLAVOR}

RUN_DEPENDS=	??/py-appdirs@${PY_FLAVOR} \
		??/py-clint@${PY_FLAVOR} \
		??/py-texttable@${PY_FLAVOR} \
		??/py-vulners@${PY_FLAVOR} \
		devel/py-six@${PY_FLAVOR} \
		lang/python


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
