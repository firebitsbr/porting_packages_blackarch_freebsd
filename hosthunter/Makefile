PORTNAME=	hosthunter
DISTVERSION=	158.553f1c7
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	A recon tool for discovering hostnames using OSINT techniques.
WWW=		https://github.com/SpiderLabs/HostHunter

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git

RUN_DEPENDS=	??/py-fake-useragent@${PY_FLAVOR} \
		??/py-pyopenssl@${PY_FLAVOR} \
		??/py-selenium@${PY_FLAVOR} \
		??/py-urllib3@${PY_FLAVOR} \
		??/py-validator-collection@${PY_FLAVOR} \
		lang/python \
		www/py-requests@${PY_FLAVOR}


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
