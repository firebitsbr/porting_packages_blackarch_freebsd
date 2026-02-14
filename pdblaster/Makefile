PORTNAME=	pdblaster
DISTVERSION=	4.fc8abb3
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Extract PDB file paths from large sample sets of executable files.
WWW=		https://github.com/SecurityRiskAdvisors/PDBlaster

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git

RUN_DEPENDS=	??/py-pandas@${PY_FLAVOR} \
		??/py-pefile@${PY_FLAVOR} \
		??/py-termcolor@${PY_FLAVOR} \
		lang/python


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
