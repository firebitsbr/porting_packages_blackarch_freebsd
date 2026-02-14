PORTNAME=	python-exchangelib
DISTVERSION=	5.6.0
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Client for Microsoft Exchange Web Services (EWS)
WWW=		https://github.com/ecederstrand/exchangelib

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	??/py-build@${PY_FLAVOR} \
		devel/py-pip@${PY_FLAVOR}

RUN_DEPENDS=	??/py-cached-property@${PY_FLAVOR} \
		??/py-defusedxml@${PY_FLAVOR} \
		??/py-dnspython@${PY_FLAVOR} \
		??/py-isodate@${PY_FLAVOR} \
		??/py-lxml@${PY_FLAVOR} \
		??/py-oauthlib@${PY_FLAVOR} \
		??/py-pygments@${PY_FLAVOR} \
		??/py-pytzdata@${PY_FLAVOR} \
		??/py-requests-ntlm@${PY_FLAVOR} \
		??/py-requests-oauthlib@${PY_FLAVOR} \
		??/py-tzlocal@${PY_FLAVOR}


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
