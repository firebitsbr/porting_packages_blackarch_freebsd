PORTNAME=	pepe
DISTVERSION=	13.b81889b
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Collect information about email addresses from Pastebin.
WWW=		https://github.com/woj-ciech/pepe

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git

RUN_DEPENDS=	??/py-colorama@${PY_FLAVOR} \
		??/py-elasticsearch@${PY_FLAVOR} \
		??/py-fullcontactpy@${PY_FLAVOR} \
		??/py-google@${PY_FLAVOR} \
		??/py-piplapis-python@${PY_FLAVOR} \
		??/py-pushsafer@${PY_FLAVOR} \
		??/py-pyhibp@${PY_FLAVOR} \
		??/py-urllib3@${PY_FLAVOR} \
		??/py-validate-email@${PY_FLAVOR} \
		lang/python \
		www/py-requests@${PY_FLAVOR}


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
