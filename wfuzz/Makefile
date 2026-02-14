PORTNAME=	wfuzz
DISTVERSION=	1157.2263cd0
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Utility to bruteforce web applications to find their not linked resources.
WWW=		https://github.com/xmendez/wfuzz

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git

RUN_DEPENDS=	??/py-chardet@${PY_FLAVOR} \
		??/py-future@${PY_FLAVOR} \
		??/py-lxml@${PY_FLAVOR} \
		??/py-pycurl@${PY_FLAVOR} \
		??/py-pyparsing@${PY_FLAVOR} \
		??/py-wxpython@${PY_FLAVOR} \
		devel/py-six@${PY_FLAVOR} \
		lang/python


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
