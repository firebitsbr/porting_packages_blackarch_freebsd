PORTNAME=	social-vuln-scanner
DISTVERSION=	11.91794c6
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Gathers public information on companies to highlight social engineering risk.
WWW=		https://github.com/Betawolf/social-vuln-scanner

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git

RUN_DEPENDS=	??/iotop \
		??/py-beautifulsoup4@${PY_FLAVOR} \
		??/py-editdistance@${PY_FLAVOR} \
		??/py-html2text@${PY_FLAVOR} \
		??/py-httplib2@${PY_FLAVOR} \
		??/py-oauth2@${PY_FLAVOR} \
		??/py-packaging@${PY_FLAVOR} \
		??/py-pillow@${PY_FLAVOR} \
		??/py-psutil@${PY_FLAVOR} \
		??/py-pyparsing@${PY_FLAVOR} \
		devel/py-six@${PY_FLAVOR} \
		lang/python


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
