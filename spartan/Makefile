PORTNAME=	spartan
DISTVERSION=	23.babdd7d
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Frontpage and Sharepoint fingerprinting and attack tool.
WWW=		https://github.com/sensepost/SPartan

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git

RUN_DEPENDS=	??/py-beautifulsoup4@${PY_FLAVOR} \
		??/py-ntlm3@${PY_FLAVOR} \
		??/py-requests-ntlm@${PY_FLAVOR} \
		devel/py-six@${PY_FLAVOR} \
		lang/python3 \
		www/py-requests@${PY_FLAVOR}


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
