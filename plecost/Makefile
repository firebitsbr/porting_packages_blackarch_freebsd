PORTNAME=	plecost
DISTVERSION=	104.4895e34
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Wordpress finger printer Tool.
WWW=		https://github.com/iniqua/plecost

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git \
		devel/py-setuptools@${PY_FLAVOR}

RUN_DEPENDS=	??/py-aiohttp@${PY_FLAVOR} \
		??/py-beautifulsoup4@${PY_FLAVOR} \
		??/py-chardet@${PY_FLAVOR} \
		??/py-lxml@${PY_FLAVOR} \
		??/py-simplejson@${PY_FLAVOR} \
		??/py-sphinx_rtd_theme@${PY_FLAVOR} \
		??/py-termcolor@${PY_FLAVOR} \
		lang/python


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
