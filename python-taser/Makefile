PORTNAME=	python-taser
DISTVERSION=	0.4.4
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Python module/library for retrieving taser information of domains.
WWW=		https://pypi.org/project/taser/#files

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/py-setuptools@${PY_FLAVOR}

RUN_DEPENDS=	??/py-beautifulsoup4@${PY_FLAVOR} \
		??/py-dnspython@${PY_FLAVOR} \
		??/py-ipparser@${PY_FLAVOR} \
		??/py-lxml@${PY_FLAVOR} \
		??/py-requests-ntlm@${PY_FLAVOR} \
		??/py-tldextract@${PY_FLAVOR} \
		lang/python \
		www/py-requests@${PY_FLAVOR}


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
