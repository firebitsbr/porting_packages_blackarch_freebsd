PORTNAME=	bloodhound
DISTVERSION=	v4.3.1.r60.g226f497
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Six Degrees of Domain Admin
WWW=		https://github.com/SpecterOps/BloodHound-Legacy

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	??/nodejs-electron-packager \
		archivers/unzip \
		devel/git \
		www/npm

RUN_DEPENDS=	??/jre17-openjdk-headless \
		??/neo4j-community \
		www/node


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
