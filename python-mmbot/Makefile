PORTNAME=	python-mmbot
DISTVERSION=	78.f5f5478
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Powerful malicious file triage tool for cyber responders.
WWW=		https://github.com/egaus/MaliciousMacroBot

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git \
		devel/py-setuptools@${PY_FLAVOR}

RUN_DEPENDS=	??/py-joblib@${PY_FLAVOR} \
		??/py-oletools@${PY_FLAVOR} \
		??/py-pandas@${PY_FLAVOR} \
		??/py-scikit-learn@${PY_FLAVOR} \
		??/py-scipy@${PY_FLAVOR} \
		??/py-ujson@${PY_FLAVOR}


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
