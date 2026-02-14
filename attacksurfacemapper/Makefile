PORTNAME=	attacksurfacemapper
DISTVERSION=	47.8a402ed
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Tool that aims to automate the reconnaissance process.
WWW=		https://github.com/superhedgy/AttackSurfaceMapper

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git

RUN_DEPENDS=	??/py-backoff@${PY_FLAVOR} \
		??/py-beautifulsoup4@${PY_FLAVOR} \
		??/py-censys@${PY_FLAVOR} \
		??/py-colorama@${PY_FLAVOR} \
		??/py-dnslib@${PY_FLAVOR} \
		??/py-dnspython@${PY_FLAVOR} \
		??/py-ipwhois@${PY_FLAVOR} \
		??/py-netaddr@${PY_FLAVOR} \
		??/py-pymongo@${PY_FLAVOR} \
		??/py-pyopenssl@${PY_FLAVOR} \
		??/py-requests-html@${PY_FLAVOR} \
		??/py-selenium@${PY_FLAVOR} \
		??/py-shodan@${PY_FLAVOR} \
		??/py-tld@${PY_FLAVOR} \
		??/py-trans@${PY_FLAVOR} \
		??/py-validator-collection@${PY_FLAVOR} \
		lang/python \
		www/py-requests@${PY_FLAVOR}


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
