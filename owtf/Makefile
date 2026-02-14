PORTNAME=	owtf
DISTVERSION=	v2.6.0.r161.g9a616f5
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	The Offensive (Web) Testing Framework.
WWW=		https://www.owasp.org/index.php/OWASP_OWTF

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git

RUN_DEPENDS=	??/postgresql \
		??/py-pyaml@${PY_FLAVOR} \
		??/py-virtualenv@${PY_FLAVOR} \
		??/py-yaml@${PY_FLAVOR} \
		lang/python


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
